from ._anvil_designer import P6_Old_Man_1Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import Timer
import anvil.js
import time
from .. import HashingFunction
from .. import Timer

class P6_Old_Man_1(P6_Old_Man_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """The room is dimly lit, shadows creeping into the corners as screens hum with scattered fragments of data. You, the hacker, are seated in the center of this digital web, surrounded by codes that pulse with life, as if they know something you don’t. But you do know one thing—your mission: uncover the Founder.

In the world of the Squid Game, secrets are more precious than lives. And the Founder, hidden behind layers of deception, has left faint traces that only a mind like yours can decipher. This isn’t a game of strength or survival—this is a game of intelligence, patterns, and precision.

The clues are buried deep in the numbers, encoded into decisions, hidden behind walls of data. Your weapons are linear regression models, hidden variables, and the ability to connect the invisible threads that others have missed. Somewhere within this maze of data lies the answer to the most dangerous question: Who controls the game?

The weight of the truth presses down, the room feels colder, more isolated. But the answer is there—just beyond reach. Time is ticking. Can you break the code before it’s too late?"""
    self.text_to_display2 = """<p>The room is dimly lit, shadows creeping into the corners as screens hum with scattered fragments of data. You, the hacker, are seated in the center of this digital web, surrounded by codes that pulse with life, as if they know something you don’t. But you do know one thing—your mission: <strong>uncover the Founder</strong>.</p>

<p>In the world of the Squid Game, secrets are more precious than lives. And the Founder, hidden behind layers of deception, has left faint traces that only a mind like yours can decipher. This isn’t a game of strength or survival—this is a game of intelligence, patterns, and precision.</p>

<p>The clues are buried deep in the numbers, encoded into decisions, hidden behind walls of data. Your weapons are <strong>linear regression models</strong>, hidden variables, and the ability to connect the invisible threads that others have missed. Somewhere within this maze of data lies the answer to the most dangerous question: <strong>Who controls the game?</strong></p>

<p>Find the name of the creator and escape with the money. The weight of the truth presses down, the room feels colder, more isolated. But the answer is there—just beyond reach. Time is ticking. Can you break the code before it’s too late?</p>
"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js("startTypingEffect", self.type_text)
    self.total_time = 0
    self.begin_time = False
    self.stay_alive = 0

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
      time.sleep(1)
      # Stop the typing effect
      anvil.js.call_js("stopTypingEffect")
      self.label_1.visible = False
      self.rich_text_1.visible = True
      self.rich_text_1.content = self.text_to_display2
      #make sure to add these to each puzzle
      self.card_2.visible =True
      self.card_3.visible =True
      self.card_4.visible =True
      Timer.start_time('p6')
      # anvil.server.call_s('start_timer', 'p6_start')
      self.begin_time = True
      self.time_elapsed.visible = True

  def timer_1_tick(self, **event_args):
    self.stay_alive += 1
    if self.begin_time:
      self.total_time += 1
      minutes = int(int(self.total_time)//60)
      seconds = int(int(self.total_time) % 60)
      
      self.time_elapsed.text = f"{minutes} min {seconds} sec"
    self.stay_alive += 1  
    if self.stay_alive >= 300:
      self.stay_alive = 0
      anvil.server.call_s('stay_alive')


  
  def submit_click(self, **event_args):
    if HashingFunction.hash_func(self.text_box_1.text) == 956053350:
      open_form('completion')
    else:
      alert("We tried inputting that password, but it did not work")

  def text_box_1_pressed_enter(self, **event_args):
    if HashingFunction.hash_func(self.text_box_1.text) == 956053350:
      open_form('completion')
    else:
      alert("We tried inputting that password, but it did not work")

  def instruction_file_click(self, **event_args):
    '''
    file_media = anvil.server.call('get_file','p6_file')
    if file_media is not None:
      anvil.download(file_media)
    else:
      notification = "The file could not be found."
      anvil.alert(notification)
    '''
    anvil.js.window.open("https://colab.research.google.com/drive/12atBbSM2OW3DFoVknQbw1Ct3Zl80OI72?usp=sharing", "_blank")

  