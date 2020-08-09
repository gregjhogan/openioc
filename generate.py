#!/usr/bin/env python3

import os
import re

import yaml

script_path = os.path.dirname(os.path.abspath(__file__))
def_path = os.path.join(script_path, "definitions")
for fn in os.listdir(def_path):
  print(f"processing {fn} ...")
  with open(os.path.join(def_path, fn)) as f:
    y = yaml.safe_load(f)

  bn = os.path.splitext(fn)[0]
  class_def = f"""
class {bn.capitalize()}InputOutputController:
  def __init__(self, send_func):
    self.send = send_func
"""

  start = y["_start_"]
  stop = y["_stop_"]
  for k, v in y.items():
    if k[0] == '_' and k[-1] == "_":
      continue
    print(f"- {k}")

    start_exp = re.sub(r"(.{2})", r"\\x\1", start.format(**v).encode().hex())
    stop_exp = re.sub(r"(.{2})", r"\\x\1", stop.format(**v).encode().hex())
    class_def += f"""
  def {k}(self, on):
    if on:
      msg = b"{start_exp}"
    else:
      msg = b"{stop_exp}"
    self.send({hex(v['_address_'])}, msg)
"""

  with open(os.path.join(script_path, f"{bn}.py"), "w") as o:
    o.write(class_def)
