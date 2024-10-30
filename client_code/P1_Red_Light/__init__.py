from ._anvil_designer import P1_Red_LightTemplate
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
#from anvil_extras.animation import animate, fade_out, Easing, Effect

class P1_Red_Light(P1_Red_LightTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """Player 136,

Right now, Player 48 is in the "Red Light, Green Light" stage, where every movement counts. As they inch their way forward, you need to extract a critical password that will give you access to the mainframe and help them proceed in the future games.

Your Mission:

Locate the Password: The password is buried deep within the system, hidden in the data stream. Extract the critical information before the doll turns around.
Maintain Stealth: The giant doll monitors every movement. Stay still whenever you hear music playing. Failing to do so will expose your connection.
Hack the Mainframe: Use the password to unlock the database. Once you’re in, you’ll have access to vital information for the next games.
Time is of the essence. The guards are watching, and the doll could turn around at any moment. Stay vigilant.

Embark on this journey with precision and stealth. Success means survival, Player 136.

Click the button below to get hacking and stay alive!
"""
    self.text_to_display2 = """<p><strong>Player 136,</strong></p>

<p>Right now, Player 48 is in the <strong>"Red Light, Green Light"</strong> stage, where every movement counts. As they inch their way forward, you need to extract a <strong>critical password</strong> that will give you access to the mainframe and help them proceed in the future games.</p>

<p><strong>Your Mission:</strong></p>

<ul>
    <li>Locate the <strong>Password</strong>: The password is buried deep within the system, hidden in the data stream. Extract the critical information before the doll turns around.</li>
    <li>Maintain <strong>Stealth</strong>: The giant doll monitors every movement. Stay still whenever you hear music playing. Failing to do so will expose your connection.</li>
    <li><strong>Hack the Mainframe</strong>: Use the password to unlock the database. Once you’re in, you’ll have access to vital information for the next games.</li>
</ul>

<p>Time is of the essence. The guards are watching, and the doll could turn around at any moment. <em>Stay vigilant.</em></p>

<p>Embark on this journey with precision and stealth. Success means survival, Player 136.</p>

<p><strong>Click the button below to get hacking and stay alive!</strong></p>
"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js("startTypingEffect", self.type_text)
    self.total_time = 0
    self.begin_time = False
    self.stay_alive = 0
    self.image_2.visible= False
    self.image_1.visible= True

  def type_text(self):
    # Remove cursor if it's there
    
    #instead
    #leave_effect = Effect(fade_out, duration=5500, easing=Easing.ease_out)
    #leave_effect.animate(self.image_1).wait()
    #self.image_1.remove_from_parent()
    time.sleep(4.5)
    #instead of doing false
    self.image_1.visible= False
    self.image_2.visible= True
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
      Timer.start_time('p1')
      # anvil.server.call_s('start_timer', 'p1_start')
      self.begin_time = True
      self.time_elapsed.visible = True

  
  def submit_click(self, **event_args):

    if HashingFunction.hash_func(self.text_box_1.text) == 117346317:
      open_form('P2_Glass_Steps')
    else:
      alert("We tried inputting that password, but it did not work")
    # past code:: --- 
    # if anvil.server.call_s('p1_check',self.text_box_1.text):
    #   open_form('P2_Glass_Steps')
    # else:
    #   alert("We tried inputting that password, but it did not work")
      
  def text_box_1_pressed_enter(self, **event_args):
    if HashingFunction.hash_func(self.text_box_1.text) == 117346317:
      open_form('P2_Glass_Steps')
    else:
      alert("We tried inputting that password, but it did not work")


  def instruction_file_click(self, **event_args):
    #file_media = anvil.server.call('get_file','p1_file')
    #if file_media is not None:
    #  anvil.download(file_media)
    ##else:
    #  notification = "The file could not be found."
     # anvil.alert(notification)
    anvil.js.window.open("https://colab.research.google.com/drive/1q0MWSvklaQlnHsTBpCzbkX8VQAB39Uqz?usp=sharing", "_blank")

      
  def timer_1_tick(self, **event_args):
    self.stay_alive += 1
    if self.begin_time:
      self.total_time += 1
      minutes = int(int(self.total_time)//60)
      seconds = int(int(self.total_time) % 60)
      
      self.time_elapsed.text = f"{minutes} min {seconds} sec"
    self.stay_alive += 1  
    #maybe this is causing downlink error in the code
    if self.stay_alive >= 300:
      self.stay_alive = 0
      anvil.server.call_s('stay_alive')


