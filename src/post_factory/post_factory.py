import asyncio
import time
import os

from PIL import Image, ImageDraw, ImageFont
from textwrap3 import fill

from ..adapters.carbon_adapter import CarbonAdapter
from ..utils.calculate_font_size import calculate_text_size

loop = asyncio.get_event_loop()


class PostFactory:
  description_font_size = 27
  description_lines = None

  def make_title(self, title, image):
    font_path = "./src/assets/RobotoCondensed-Bold.ttf"
    font_size, text_height = calculate_text_size(title, font_path, 800)
    font = ImageFont.truetype(font_path, size=font_size)
    drawer = ImageDraw.Draw(image)
    drawer.text((200, 80), title.upper(), (255, 255, 255), font=font)

    return text_height

  def make_description(self, description, image, title_text_height = 0): 
    font = ImageFont.truetype("./src/assets/OpenSauceOne-Light.ttf", size=self.description_font_size)
    drawer = ImageDraw.Draw(image)

    wrapped_text = "\n".join(x for x in fill(text=description, width=70).splitlines())
    self.description_lines = len(wrapped_text.split('\n'))

    drawer.text((200, title_text_height + 110), wrapped_text, (255, 255, 255), font=font)

  def make_code_block(self, code_file_content, image):
    y_pos = 280

    if self.description_lines:
      y_pos = y_pos + (self.description_lines * self.description_font_size)
    
    file_path = f'tmp/code-{time.time()}.png'
    carbon_adapter = CarbonAdapter('\n'.join(code_file_content.split('\n')), file_path)

    loop.run_until_complete(carbon_adapter.make())

    code_block = Image.open(file_path)

    image.paste(code_block, (190, y_pos), code_block.convert('RGBA'))
    os.remove(file_path)
