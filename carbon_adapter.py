import json

import requests

import utils


class CarbonAdapter:
  def __init__(self, code, output_path):
    self.code = code
    self.output_path = output_path

  async def make(self):
    result = requests.post('https://carbonara-42.herokuapp.com/api/cook',
      headers={ 'Content-Type': 'application/json' },
      data=json.dumps({
        "code": self.code,
        "backgroundColor": "#000000",
        "theme": "one-dark",
        "width": 420,
        "widthAdjustment": False,
        "paddingHorizontal": '0px',
        "paddingVertical": '0px',
      }),
      stream=True
    )
    
    if result.status_code == 200:
      with open(self.output_path, 'wb') as output:
        for chunk in result:
          output.write(chunk)
    else:
      utils.log_error("Failed to create code block image!", "Cannot make your code beauty, please try again!")
