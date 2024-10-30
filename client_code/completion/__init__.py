from ._anvil_designer import completionTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import Timer
from .. import Timer


class completion(completionTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.elapsed = Timer.end_time()
    Timer.commit_times()
    # self.elapsed = anvil.server.call_s('stop_timer')
    self.elapsed1 = str(int(self.elapsed//60)) + ' min ' + str(int(self.elapsed % 60)) + ' sec'
    self.text_to_display1 = f"""Congratulations, Player 136!
You’ve done it! Through cunning, strategy, and sheer determination, you have successfully guided Player 48 to victory in the Squid Game.

Your remarkable skills have not only brought Player 48 to safety but also triumphed over the countless dangers along the way. You completed this ultimate challenge in {self.elapsed1}.

Now, sit back and revel in the glory. BAXA is tallying the final results as we speak. Soon, we’ll know who the true masterminds of the Escape McCombs: Squid Game Edition are.

Thank you for your incredible dedication and for seeing this through to the end. Victory is yours!

"""
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

