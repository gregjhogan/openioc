
class HondaInputOutputController:
  def __init__(self, send_func):
    self.send = send_func

  def left_turn_signal(self, on):
    if on:
      msg = b"\x30\x0a\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def right_turn_signal(self, on):
    if on:
      msg = b"\x30\x0b\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def hazard_lights(self, on):
    if on:
      msg = b"\x30\x08\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def parking_lights(self, on):
    if on:
      msg = b"\x30\x25\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def headlight_low_beams(self, on):
    if on:
      msg = b"\x30\x1c\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def headlight_high_beams(self, on):
    if on:
      msg = b"\x30\x1d\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def front_fog_lights(self, on):
    if on:
      msg = b"\x30\x20\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def daytime_running_lights(self, on):
    if on:
      msg = b"\x30\x36\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def lock_all_doors(self, on):
    if on:
      msg = b"\x30\x04\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def unlock_all_doors(self, on):
    if on:
      msg = b"\x30\x05\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def unlock_all_doors_alt(self, on):
    if on:
      msg = b"\x30\x06\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def trunk_release(self, on):
    if on:
      msg = b"\x30\x09\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def front_wipers_slow(self, on):
    if on:
      msg = b"\x30\x19\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def front_wipers_fast(self, on):
    if on:
      msg = b"\x30\x1a\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def front_washer_pump(self, on):
    if on:
      msg = b"\x30\x1b\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def rear_wiper(self, on):
    if on:
      msg = b"\x30\x0d\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def rear_washer_pump(self, on):
    if on:
      msg = b"\x30\x0e\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def left_blind_spot_indicator(self, on):
    if on:
      msg = b"\x30\x01\x08\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f19ff0, msg)
