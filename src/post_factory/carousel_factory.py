import base64
import os

from PIL import Image, ImageDraw, ImageFont
from textwrap3 import fill

from .post_factory import PostFactory

class CarouselFactory(PostFactory):
  title_layer = None
  code_block_layer = None
  base_image: Image

  def __init__(self, post_data):
    self.title_base_image = Image.open('./src/assets/base-firstpost-v1.png')
    self.post_data = post_data
    
  def make(self):
    self.make_title_post()
    self.make_all_content_posts()

    return self.base_image

  def make_title_post(self):
    font = ImageFont.truetype("./src/assets/RobotoCondensed-Bold.ttf", size=100)
    drawer = ImageDraw.Draw(self.title_base_image)

    wrapped_text = "\n".join(fill(text=self.post_data['title'].upper(), width=15).splitlines())
    
    max_line_length = max([len(line) for line in wrapped_text.split('\n')])

    margins = 15
    content_x_pos = 120
    content_y_pos = 350
    
    max_line_length = 700
    line_length = (max_line_length * 60) + margins
    line_length = line_length if line_length < max_line_length else max_line_length

    text_y_pos = content_y_pos - ((len(wrapped_text.split('\n')) - 1) * 100)
    line_y_pos = content_y_pos + margins + 100

    drawer.text((content_x_pos + margins, text_y_pos), wrapped_text, (247, 244, 240), font=font)
    drawer.line((content_x_pos, line_y_pos, content_x_pos + line_length, line_y_pos), fill=(211, 192, 167), width=3)

    # self.title_base_image.save(f'{self.post_folder_path}/output/0.png')

  def make_all_content_posts(self):
    for index, content in enumerate(self.post_data['content']):
      post_image = Image.open('./src/assets/base-v1.png')

      self.make_title(content['title'], post_image)
      self.make_description(content['text'], post_image)

      if 'code' in content.keys():
        self.make_code_block(content['code'], post_image)

      # post_image.save(f'{self.post_folder_path}/output/{index + 1}.png')

  
