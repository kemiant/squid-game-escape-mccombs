from ._anvil_designer import WelcomeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Welcome(WelcomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display = """Welcome to Escape McCombs: Art Heist!

Greetings, everyone!

You are about to embark on a thrilling adventure, crafted specially by BAXA - UT's Business Analytics Association.

As you dive into the mysteries that await, remember that while competition is fierce, collaboration and honor are paramount.

Rules & Guidelines:
  1. Fair Play: No sabotaging other teams. Let's maintain a competitive yet respectful environment.
  
  2. Use of Tools: While the internet is at your disposal, using ChatGPT or any other AI/ML models for assistance is strictly prohibited. We value human ingenuity and problem-solving skills in this challenge.
  
  3. Submission Protocol: For any textbox, the way to submit your answer is to press enter within the textbox. Ensure your entries are accurate before submission.
  
  4. Platform Etiquette: Given the technical constraints of the platform, Anvil might occasionally exhibit lag. We request your patience. Please refrain from spamming the 'enter' or 'submit' buttons. Give the system a few moments to process your actions.


Best of luck, agents! Dive in, and may the best team prevail!"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js('startTypingEffect', self.type_text)



  def type_text(self):
    # Remove cursor if it's there
    if self.label_1.text.endswith('▮'):
      self.label_1.text = self.label_1.text[:-1]

    if self.current_position < len(self.text_to_display):
      # Append next character to label's text
      self.label_1.text += self.text_to_display[self.current_position]
      self.current_position += 1
      # Add cursor
      self.label_1.text += '▮'
    else:
      # Stop the typing effect
      self.text_box_1.visible = True
      anvil.js.call_js('stopTypingEffect')
    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    team_name = self.text_box_1.text
    # anvil.server.call_s('register_team', team_name)
    # open_form('C1_IdentifyArt')
    
    response = anvil.server.call('register_or_resume_team', team_name)
    
    # Check the response status
    if response['status'] == 'resumed':
        # The team is resuming, open the last started form
        open_form(response['last_started_form'])
    elif response['status'] == 'registered':
        # This is a new team, start with the first challenge
        open_form('C1_IdentifyArt')
