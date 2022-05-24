import os
import sys

from post_handler import PostHandler
from template_handler import TemplateHandler


class CliInterface:
  handlersMap = ["post", "template"]
  args: list[str]
  
  action: str
  sub_action: str

  def __init__(self):
    self.args = sys.argv[1:]
    self.action = self.args[0]
    
    try:
      self.sub_action = self.args[1]
    except IndexError:
      self.sub_action = None

    if self.action == "-h":
      return self.help_handler()

    if self.action not in self.handlersMap:
      raise ValueError("Invalid action: %s" % self.action)

    getattr(self, '%s_handler' % self.action)()

  def get_flag_value(self, flag):
    try:
      return next(self.args[i + 1] for i, arg in enumerate(self.args) if arg == '--%s' % flag)
    except StopIteration:
      raise AttributeError("Invalid flag value for \"%s\"" % flag) 

  # TODO
  def help_handler(self): print("""Help: To be done 🚀""")

  def post_handler(self):
    sub_actions = {
      "clear": lambda: os.popen("rm -rf posts/**")
    }

    if self.sub_action in sub_actions.keys():
      return sub_actions[self.sub_action]()

    post_id = self.get_flag_value('id')

    PostHandler(post_id)

  def template_handler(self):
    post_type = self.get_flag_value('type')
    post_title = self.get_flag_value('title')

    TemplateHandler(
      type=post_type,
      title=post_title,
    )
    
CliInterface()
