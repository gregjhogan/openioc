
class HyundaiInputOutputController:
  def __init__(self, send_func):
    self.send = send_func

  def front_wipers_slow(self, on):
    if on:
      msg = b"\x04\x2f\xb0\x08\x03"
    else:
      msg = b"\x04\x2f\xb0\x08\x00\x00"
    self.send(0x700, msg)

  def front_wipers_fast(self, on):
    if on:
      msg = b"\x04\x2f\xb0\x09\x03"
    else:
      msg = b"\x04\x2f\xb0\x09\x00\x00"
    self.send(0x700, msg)

  def rear_wiper(self, on):
    if on:
      msg = b"\x04\x2f\xb0\x0a\x03"
    else:
      msg = b"\x04\x2f\xb0\x0a\x00\x00"
    self.send(0x700, msg)

  def surround_view_rear_wide(self, on):
    if on:
      msg = b"\x05\x2f\xf0\x12\x07\xff"
    else:
      msg = b"\x05\x2f\xf0\x12\x00\x00"
    self.send(0x793, msg)

  def surround_view_front_wide(self, on):
    if on:
      msg = b"\x05\x2f\xf0\x13\x07\xff"
    else:
      msg = b"\x05\x2f\xf0\x13\x00\x00"
    self.send(0x793, msg)

  def surround_view_rear_above(self, on):
    if on:
      msg = b"\x05\x2f\xf0\x20\x07\xff"
    else:
      msg = b"\x05\x2f\xf0\x20\x00\x00"
    self.send(0x793, msg)

  def surround_view_front_above(self, on):
    if on:
      msg = b"\x05\x2f\xf0\x21\x07\xff"
    else:
      msg = b"\x05\x2f\xf0\x21\x00\x00"
    self.send(0x793, msg)

  def surround_view_rear_side(self, on):
    if on:
      msg = b"\x05\x2f\xf0\x24\x07\xff"
    else:
      msg = b"\x05\x2f\xf0\x24\x00\x00"
    self.send(0x793, msg)

  def surround_view_front_side(self, on):
    if on:
      msg = b"\x05\x2f\xf0\x25\x07\xff"
    else:
      msg = b"\x05\x2f\xf0\x25\x00\x00"
    self.send(0x793, msg)
