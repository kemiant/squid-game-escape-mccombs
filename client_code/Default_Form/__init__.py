from ._anvil_designer import Default_FormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import Timer
import anvil.js


class Default_Form(Default_FormTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """"""
    self.text_to_display2 = """"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js('startTypingEffect', self.type_text)


  def type_text(self):
    # Remove cursor if it's there
    if self.label_1.text.endswith('▮'):
      self.label_1.text = self.label_1.text[:-1]

    if self.current_position < len(self.text_to_display1):
      # Append next character to label's text
      self.label_1.text += self.text_to_display1[self.current_position]
      self.current_position += 1
      # Add cursor
      self.label_1.text += '▮'
    else:
      # Stop the typing effect
      anvil.js.call_js('stopTypingEffect')
      self.label_1.visible = False
      self.rich_text_1.visible = True
      self.rich_text_1.content = self.text_to_display2


  def submit_click(self, **event_args):
    combination_value = self.combination_lock_form.get_combination()
    if anvil.server.call_s('',combination_value):
      open_form('')