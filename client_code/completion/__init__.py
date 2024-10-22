from ._anvil_designer import CompletionTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import Timer


class Completion(CompletionTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.elapsed = anvil.server.call_s('stop_timer')
    self.elapsed1 = str(int(self.elapsed//60)) + ' min ' + str(int(self.elapsed % 60)) + ' sec'
    self.text_to_display1 = f"""Congrats! We have successfully stolen Mac Gourbing's Assets.
    
You completed this Escape McCombs in {self.elapsed1}.
    
Please remain seated while BAXA tallies up all team times. We'll soon determine the top performers of the Escape McCombs: Heisting Halls Edition.

Thank you for your participation and dedication."""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js('startTypingEffect', self.type_text)
    self.card_3.visible = True

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

