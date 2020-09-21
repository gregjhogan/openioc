#!/usr/bin/env python3

import time

from panda.python import Panda
from hyundai import HyundaiInputOutputController

BUS = 0 # must be C-CAN bus for Honda

p = Panda()
ioc = HyundaiInputOutputController(lambda addr, dat: p.can_send(addr, dat, BUS))

print("surround view ...")
ioc.surround_view_rear_wide(True)
time.sleep(10)
ioc.surround_view_rear_wide(False)
