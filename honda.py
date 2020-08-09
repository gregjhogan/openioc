
class HondaInputOutputController:
  def __init__(self, send_func):
    self.send = send_func

  def rightTurnSignal(self, on):
    if on:
      msg = b"\x30\x0b\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def leftTurnSignal(self, on):
    if on:
      msg = b"\x30\x0a\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def hazardLights(self, on):
    if on:
      msg = b"\x30\x08\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)
