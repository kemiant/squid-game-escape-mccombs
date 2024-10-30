from ._anvil_designer import Welcome_Part1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time

class Welcome_Part1(Welcome_Part1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display = """The promise of wealth is tantalizing—life-changing money for those who make it to the end. But understand this: only the cleverest, the most determined, and the most resourceful will have any chance of walking out with their life and fortune.

Do you have what it takes? Will you risk it all for a chance at glory and unimaginable wealth?
"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js("startTypingEffect", self.type_text)

  def type_text(self):
    #time.sleep(4)
    # Remove cursor if it's there
    if self.label_1.text.endswith("▮"):
      self.label_1.text = self.label_1.text[:-1]

    if self.current_position < len(self.text_to_display):
      # Append next character to label's text
      self.label_1.text += self.text_to_display[self.current_position]
      self.current_position += 1
      # Add cursor
      self.label_1.text += "▮"
    else:
      # Stop the typing effect
      anvil.js.call_js("stopTypingEffect")
      self.button_1.visible = True
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Welcome')
