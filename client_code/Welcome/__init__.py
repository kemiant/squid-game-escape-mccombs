from ._anvil_designer import WelcomeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import Timer

class Welcome(WelcomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display = """Welcome to the Escape McCombs: Squid Game
Greetings, Player 136.

You’ve been selected to play a dangerous and high-stakes game, not for yourself, but to help Player 48 survive. The rules of the Squid Game may be cruel, but you hold a powerful advantage. As a hacker, your role is to provide guidance and cheats through the complexities ahead. Every line of code you solve brings Player 48 one step closer to victory.

The path is treacherous. Challenges will come your way, riddles of logic, puzzles of code, and only through your skill can Player 48 navigate the horrors of this game. But remember—this is not just a challenge of intelligence; it’s a test of wit and timing.

Are you ready to face the dangers of the Squid Game and help Player 48 escape with their life... and the fortune?

Rules & Guidelines:
Fair Play:
No sabotaging other teams. Let's maintain a competitive yet respectful environment.

Use of Tools:
While the internet is at your disposal, using ChatGPT or any other AI/ML models for assistance is strictly prohibited. We value human ingenuity and problem-solving skills in this challenge.

Submission Protocol:
For any textbox, the way to submit your answer is to press enter within the textbox. Ensure your entries are accurate before submission.

Platform Etiquette:
Given the technical constraints of the platform, Anvil might occasionally exhibit lag. We request your patience. Please refrain from spamming the 'enter' or 'submit' buttons. Give the system a few moments to process your actions.

Good luck, Player 136. The future of Player 48 rests in your hands."""
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
    
    # response = anvil.server.call('register_or_resume_team', team_name)
    Timer.set_team_name(team_name)
    response = Timer.start_resume_team()

    # Check the response status
    if response['status'] == 'resumed' and response['last_started_form']:
        # The team is resuming, open the last started form
      open_form(response['last_started_form'])
    elif response['status'] == 'registered':
        # This is a new team, start with the first challenge
        open_form('P1_Red_Light')
    else:
      open_form('P1_Red_Light')
