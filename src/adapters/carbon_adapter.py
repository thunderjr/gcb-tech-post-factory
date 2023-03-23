import carbonsh

from ..utils.log import log_error

class CarbonAdapter:
  def __init__(self, code, output_path):
    self.code = code
    self.output_path = output_path

  async def make(self):
    try:
      config = carbonsh.Config(
        background_color="#000000",
        theme="one-dark"
      )
      config._pv = "0px"
      config._ph = "0px"
      config._wa = False
      config._width = 420
      
      await carbonsh.code_to_file(
        self.code,
        config,
        self.output_path,
        headless=True
      )
    except Exception as e:
      log_error("Failed to create code block image!", "Cannot make your code beauty, please try again!")
      print(e)
