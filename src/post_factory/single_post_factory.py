import os

from PIL import Image
import base64

from .post_factory import PostFactory


class SinglePostFactory(PostFactory):
  title: str
  code = None
  
  title_layer = None
  code_block_layer = None

  base_image: Image

  def __init__(self, post_data):
    print(os.getcwd())
    self.base_image = Image.open('./src/assets/base-v1.png')
    self.title = post_data.get('title')
    self.text = post_data.get('text')
    self.code = post_data.get('code', None)
       
  def make(self):
    title_text_height = self.make_title(self.title.upper(), self.base_image)
    self.make_description(self.text, self.base_image, title_text_height)
    if self.code:
      self.make_code_block(self.code, self.base_image)

    # self.base_image.save(f'{self.post_folder_path}/output/post.png')
    return self.base_image
