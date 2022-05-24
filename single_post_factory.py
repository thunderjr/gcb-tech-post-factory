import os

from PIL import Image

import utils
from post_factory import PostFactory


class SinglePostFactory(PostFactory):
  title: str
  code_file_content = None
  
  title_layer = None
  code_block_layer = None

  post_folder_path: str
  base_image: Image

  def __init__(self, folder_path, post_data):
    self.base_image = Image.open('assets/base-v1.png')
    self.post_folder_path = folder_path
    self.title = post_data['title']
    self.text = post_data['text']
    
    if 'code_file' in post_data.keys():
      try:
        with open(f"{folder_path}/{post_data['code_file']}") as code_file:
          self.code_file_content = ''.join(code_file.readlines())
      except:
        utils.log_error("Error reading code file!", "The specified file path could not be located, please provide a valid file path and try again.")
        return
    
    os.makedirs(os.path.dirname(f'{self.post_folder_path}/output/'), exist_ok=True)

    self.make()
  
  def make(self):
    self.make_title(self.title.upper(), self.base_image)
    self.make_description(self.text, self.base_image)
    self.make_code_block(self.code_file_content, self.base_image)

    self.base_image.save(f'{self.post_folder_path}/output/post.png')
