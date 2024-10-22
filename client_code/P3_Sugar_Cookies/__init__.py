from ._anvil_designer import P3_Sugar_CookiesTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import Timer
import anvil.js


class P3_Sugar_Cookies(P3_Sugar_CookiesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """Hello"""
    self.text_to_display2 = """"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js("startTypingEffect", self.type_text)

  def type_text(self):
    # Remove cursor if it's there
    if self.label_1.text.endswith("▮"):
      self.label_1.text = self.label_1.text[:-1]

    if self.current_position < len(self.text_to_display1):
      # Append next character to label's text
      self.label_1.text += self.text_to_display1[self.current_position]
      self.current_position += 1
      # Add cursor
      self.label_1.text += "▮"
    else:
      anvil.js.call_js('stopTypingEffect')
      self.flow_panel_1.visible = True
      anvil.server.call_s('start_timer', 'c3_start')
      self.card_3.visible = True

  def submit_click(self, **event_args):
    combination_value = self.combination_lock_form.get_combination()
    if anvil.server.call_s("", combination_value):
      open_form("")

  def pandas_click(self, **event_args):
      file_media = anvil.server.call('get_file','C1_Pandas')
      if file_media is not None:
        anvil.download(file_media)
      else:
        notification = "The file could not be found."
        anvil.alert(notification)


  def text_box_1_pressed_enter(self, **event_args):
    if anvil.server.call_s('p3_check',self.text_box_1.text):
      open_form('P4_Tug_War')
    else:
      alert("We tried inputting that password, but it did not work")

  def label_1_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass
