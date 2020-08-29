#!/usr/bin/env python3

import os
import re

import yaml

script_path = os.path.dirname(os.path.abspath(__file__))
for p in os.listdir(script_path):
  def_path = os.path.join(script_path, p)
  if p[0] == "." or not os.path.isdir(p):
    continue

  print(f"processing {p} ...")
  with open(os.path.join(def_path, "definition.yaml")) as f:
    y = yaml.safe_load(f)

  class_def = f"""
class {p.capitalize()}InputOutputController:
  def __init__(self, send_func):
    self.send = send_func
"""

  start = y["_start_"]
  stop = y["_stop_"]
  for k, v in y.items():
    if k[0] == '_' and k[-1] == "_":
      continue
    print(f"- {k}")

    start_exp = re.sub(r"(.{2})", r"\\x\1", start.format(**v).encode('charmap').hex())
    stop_exp = re.sub(r"(.{2})", r"\\x\1", stop.format(**v).encode('charmap').hex())
    if "_instant_" in v.keys():
      class_def += f"""
  def {k}(self):
    self.send({hex(v['_address_'])}, b"{start_exp}")
"""
    else:
      class_def += f"""
  def {k}(self, on):
    if on:
      msg = b"{start_exp}"
    else:
      msg = b"{stop_exp}"
    self.send({hex(v['_address_'])}, msg)
"""

  with open(os.path.join(def_path, "__init__.py"), "w") as o:
    o.write(class_def)
