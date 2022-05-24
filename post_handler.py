import os
import json
from carousel_factory import CarouselFactory
from single_post_factory import SinglePostFactory

posts_folder = 'posts'

class PostHandler:
  id: int
  title: str
  type: str
  
  folder_path: str
  post_data: dict

  def __init__(self, id: int):
    self.id = id
    self.folder_path = self.get_post_folder()
    
    self.get_post_data()

    getattr(self, "%s_handler" % self.post_data['type'])()

  def get_post_folder(self):
    return next(f'{posts_folder}/{filename}' for filename in next(os.walk('posts'))[1] if filename.endswith(self.id))
  
  def get_post_data(self):
    post_data_file = open("%s/post_data.json" % self.folder_path, 'r')
    self.post_data = json.loads("\n".join(post_data_file.readlines()))

  def carousel_handler(self):
    CarouselFactory(self.folder_path, self.post_data)

  def single_handler(self):
    SinglePostFactory(self.folder_path, self.post_data)