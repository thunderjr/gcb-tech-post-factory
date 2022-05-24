import asyncio
import os

from PIL import Image, ImageDraw, ImageFont
from textwrap3 import fill

from carbon_adapter import CarbonAdapter

loop = asyncio.get_event_loop()


class PostFactory:
  description_font_size = 26
  description_lines = None

  def make_title(self, title, image):
    font = ImageFont.truetype("assets/RobotoCondensed-Bold.ttf", size=90)
    drawer = ImageDraw.Draw(image)
    drawer.text((200, 80), title.upper(), (255, 255, 255), font=font)

  def make_description(self, description, image): 
    font = ImageFont.truetype("assets/OpenSauceOne-Light.ttf", size=self.description_font_size)
    drawer = ImageDraw.Draw(image)

    wrapped_text = "\n".join(x for x in fill(text=description, width=60).splitlines())
    self.description_lines = len(wrapped_text.split('\n'))

    drawer.text((200, 200), wrapped_text, (255, 255, 255), font=font)

  def make_code_block(self, code_file_content, image):
    y_pos = 280

    if self.description_lines:
      y_pos = y_pos + (self.description_lines * self.description_font_size)
    
    file_path = f'{self.post_folder_path}/output/code.png'
    carbon_adapter = CarbonAdapter('\n'.join(code_file_content.split('\n')), file_path)

    loop.run_until_complete(carbon_adapter.make())

    code_block = Image.open(file_path)

    image.paste(code_block, (190, y_pos), code_block.convert('RGBA'))
    os.remove(file_path)
