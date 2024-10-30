from ._anvil_designer import P3_Sugar_CookiesTemplate
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

class P3_Sugar_Cookies(P3_Sugar_CookiesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.text_to_display1 = """The Hidden Puzzle
….___________________________________________________________________________________________________________________________________________________________….
The path ahead is not as simple as it seems. Three symbols are known, but one is missing—a shape that holds the key to your survival. To find the next clue, you must first discover what this elusive shape is and where it leads.
Clue 1:
“Three shapes are bound to the earth, their edges familiar. But a fourth rises above, guiding those who seek it when the world fades to black.”
The circle, the triangle, and the square—these shapes have been seen before. Yet, there is one more, one that stands above them all..
But the shapes alone will not guide you. Hidden in the very letters of this message lies another truth, one you cannot see but can feel—a rhythm that taps, clicks, and pauses. Once unlocked, find the room to where the truth leads to, and then the shapes will help you from there on.
--. ... -...   ...-- .---- ..--- ---..          ____________…
"""
    self.text_to_display2 = """  
    <p>--. ... -...   ...-- .---- ..--- ---..                        ________________________________________________________________________</p>
    <h2>The Hidden Puzzle</h2>
  <hr>
  <p>The path ahead is not as simple as it seems. Three symbols are known, but one is missing—a shape that holds the key to your survival. To find the next clue, you must first discover what this elusive shape is and where it leads.</p>
  <br>
  <h3>Clue 1:</h3>
  <p><em>“Three shapes are bound to the earth, their edges familiar. But a fourth rises above, guiding those who seek it when the world fades to black.”</em></p>
  
  <p>The circle, the triangle, and the square—these shapes have been seen before. Yet, there is one more, one that stands above them all.</p>
  
  <p>But the shapes alone will not guide you. Hidden in the very letters of this message lies another truth, one you cannot see but can feel—a rhythm that taps, clicks, and pauses. The hidden message will lead you to a room, find the room to where the truth leads to, and then tell the shape to the guard and they will help you from there on.</p>
  <br>
  <p>--. ... -...   ...-- .---- ..--- ---..                        ________________________________________________________________________</p>
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
      
      # Stop the typing effect
      anvil.js.call_js("stopTypingEffect")
      self.label_1.visible = False
      self.rich_text_1.visible = True
      self.rich_text_1.content = self.text_to_display2
      #make sure to add these to each puzzle
     # self.card_2.visible =True
      self.card_3.visible =True
      self.card_4.visible =True
      Timer.start_time('p3')
      # anvil.server.call_s('start_timer', 'p3_start')
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
    if HashingFunction.hash_func(self.text_box_1.text) == 495700216:
      open_form('P4_Tug_War')
    else:
      alert("We tried inputting that password, but it did not work")

  def text_box_1_pressed_enter(self, **event_args):
    if HashingFunction.hash_func(self.text_box_1.text) == 495700216:
      open_form('P4_Tug_War')
    else:
      alert("We tried inputting that password, but it did not work")

  
  def instruction_file_click(self, **event_args):
    file_media = anvil.server.call('get_file','p3_file')
    if file_media is not None:
      anvil.download(file_media)
    else:
      notification = "The file could not be found."
      anvil.alert(notification)



