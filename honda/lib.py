
class HondaInputOutputController:
  def __init__(self, send_func):
    self.send = send_func

  def leftTurnSignal(self, on):
    if on:
      msg = b"\x30\x0a\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def rightTurnSignal(self, on):
    if on:
      msg = b"\x30\x0b\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def hazardLights(self, on):
    if on:
      msg = b"\x30\x08\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def parkingLights(self, on):
    if on:
      msg = b"\x30\x25\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def headlightLowBeams(self, on):
    if on:
      msg = b"\x30\x1c\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def headlightHighBeams(self, on):
    if on:
      msg = b"\x30\x1d\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def frontFogLights(self, on):
    if on:
      msg = b"\x30\x20\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def daytimeRunningLights(self, on):
    if on:
      msg = b"\x30\x36\x0f\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def lockAllDoors(self, on):
    if on:
      msg = b"\x30\x04\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def unlockAllDoors(self, on):
    if on:
      msg = b"\x30\x05\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def unlockAllDoorsAlt(self, on):
    if on:
      msg = b"\x30\x06\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def trunkRelease(self, on):
    if on:
      msg = b"\x30\x09\x01\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def frontWipersSlow(self, on):
    if on:
      msg = b"\x30\x19\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def frontWipersFast(self, on):
    if on:
      msg = b"\x30\x1a\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def frontWasherPump(self, on):
    if on:
      msg = b"\x30\x1b\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def rearWiper(self, on):
    if on:
      msg = b"\x30\x0d\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def rearWasherPump(self, on):
    if on:
      msg = b"\x30\x0e\x05\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f118f0, msg)

  def leftBlindSpotIndicator(self, on):
    if on:
      msg = b"\x30\x01\x08\x00\x00\x00\x00\x00"
    else:
      msg = b"\x20"
    self.send(0x16f19ff0, msg)
