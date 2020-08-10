#!/usr/bin/env python3

import time

from panda import Panda
from honda import HondaInputOutputController

BUS = 1 # must be B-CAN bus for Honda

p = Panda()
ioc = HondaInputOutputController(lambda addr, dat: p.can_send(addr, dat, BUS))
print("lock all doors ...")
ioc.lock_all_doors()
time.sleep(1)
print("unlock all doors ...")
ioc.unlock_all_doors()
time.sleep(1)
print("right turn signal ...")
ioc.right_turn_signal(True)
time.sleep(1)
ioc.right_turn_signal(False)
time.sleep(0.2)
print("left turn signal ...")
ioc.left_turn_signal(True)
time.sleep(1)
ioc.left_turn_signal(False)
time.sleep(0.2)
print("headlight low beams ...")
ioc.headlight_low_beams(True)
time.sleep(1)
ioc.headlight_low_beams(False)
time.sleep(0.2)
print("headlight high beams ...")
ioc.headlight_high_beams(True)
time.sleep(1)
ioc.headlight_high_beams(False)
