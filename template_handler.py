import json
import os
from datetime import datetime

import utils


class TemplateHandler:
  post_title: str
  post_type: str
  folder_path: str

  def __init__(self, type: str, title: str, **kwargs):
    now = int(datetime.now().timestamp())
    self.folder_path = 'posts/%s-%s' % (title, now)
    self.post_title = title
    
    parsed_post_data = self.make_post_data(type)

    os.makedirs(os.path.dirname(f"{self.folder_path}/"), exist_ok=True)
    
    with open("%s/post_data.json" % self.folder_path, "w") as post_data_file:
      post_data_file.writelines(json.dumps(parsed_post_data, indent=4))

    with open("%s/example_code.ts" % self.folder_path, "w") as sample_code_example_file:
      with open("assets/example-code.ts", "r") as sample_code_data_file:
        sample_code_example_file.writelines(sample_code_data_file.readlines())
    
    utils.log_success("Template generated!", f"Setup your files and use this id: {now} to generate your post!")

  def make_post_data(self, type):
    if type == 'carousel':
      return json.loads("""{
        "title": "%s",
        "type": "carousel",
        "content": [{
          "title": "Exemple Title",
          "text": "Some content to our example, this will be put before the code image",
          "code_file": "./example_code.ts"
        }]
      }""" % self.post_title)
    elif type == 'single':
      return json.loads("""{
        "title": "%s",
        "type": "single",
        "text": "Some content to our example, this will be put before the code image",
        "code_file": "./example_code.ts"
      }""" % self.post_title)
