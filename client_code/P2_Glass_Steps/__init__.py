from ._anvil_designer import P2_Glass_StepsTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
# from anvil import Timer
import anvil.js
import time
from .. import HashingFunction
from .. import Timer


class P2_Glass_Steps(P2_Glass_StepsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """Welcome to the Glass Stepping Game

In the world of the Squid Game, every step can mean the difference between life and death. The Glass Stepping Game is no exception. Players must navigate a deadly bridge made of fragile glass tiles, where only one path is safe. Each wrong step shatters the glass beneath them, sending them to their doom.
This time, Player 48 is at the mercy of your skills. But instead of simply watching, you are given a different task. As their trusted hacker, you must guide them safely across the glass by hacking into the Squid Game’s player database. The information you uncover will help you decide which tiles are safe and which ones will shatter.
Your mission is clear: clean the data and extract the vital information needed to save Player 48. Each step you take in the data cleaning process brings you closer to identifying the correct glass tiles they must step on.
The fate of Player 48 is in your hands. The clock is ticking, and the glass bridge is waiting. Will your data cleaning skills be enough to lead them safely across?"""
    self.text_to_display2 = """<h1>Welcome to the Glass Stepping Game</h1>

<p>In the world of the Squid Game, every step can mean the difference between life and death. The Glass Stepping Game is no exception. Players must navigate a deadly bridge made of fragile glass tiles, where only one path is safe. Each wrong step shatters the glass beneath them, sending them to their doom.</p>

<p>This time, <strong>Player 48</strong> is at the mercy of your skills. But instead of simply watching, you are given a different task. As their trusted hacker, you must <em>guide them safely</em> across the glass by hacking into the Squid Game’s player database. The information you uncover will help you decide which tiles are safe and which ones will shatter.</p>

<p>Your mission is clear: <strong>clean the data</strong> and extract the vital information needed to save Player 48. Each step you take in the data cleaning process brings you closer to identifying the correct glass tiles they must step on.</p>

<p>The fate of Player 48 is in your hands. The clock is ticking, and the glass bridge is waiting. Will your data cleaning skills be enough to lead them safely across?</p>

<p>Input each player ID position in the same order with no spaces.</p>
"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    self.image_2.visible = True
    anvil.js.call_js("startTypingEffect", self.type_text)
    self.total_time = 0
    self.begin_time = False
    self.stay_alive = 0
    
    

  def type_text(self):
    time.sleep(4.5)
    self.image_2.visible = False
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
      # Stop the typing effect
      time.sleep(1)
      anvil.js.call_js("stopTypingEffect")
      self.label_1.visible = False
      self.rich_text_1.visible = True
      self.rich_text_1.content = self.text_to_display2
      #make sure to add these to each puzzle
      self.card_2.visible =True
      self.card_3.visible =True
      self.card_4.visible =True
      Timer.start_time('p2')
      # anvil.server.call_s('start_timer', 'p2_start')
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
    if HashingFunction.hash_func(self.text_box_1.text) == 4258531534:
      open_form('P3_Sugar_Cookies')
    else:
      alert("We tried inputting that password, but it did not work")

  def text_box_1_pressed_enter(self, **event_args):
    if HashingFunction.hash_func(self.text_box_1.text) == 4258531534:
      open_form('P3_Sugar_Cookies')
    else:
      alert("We tried inputting that password, but it did not work")
    # if anvil.server.call_s('p2_check',self.text_box_1.text):
    #   open_form('P3_Sugar_Cookies')
    # else:
    #   alert("We tried inputting that password, but it did not work")
      

  def instruction_file_click(self, **event_args):
    '''
    file_media = anvil.server.call('get_file','p2_file')
    if file_media is not None:
      anvil.download(file_media)
    else:
      notification = "The file could not be found."
      anvil.alert(notification)
    '''
    anvil.js.window.open("https://colab.research.google.com/drive/1f56MV60gdr__45PtoHlcQLZBfDjX0kXs?usp=sharing", "_blank")
