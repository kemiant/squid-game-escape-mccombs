from ._anvil_designer import P4_Tug_WarTemplate
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

class P4_Tug_War(P4_Tug_WarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """Mission Brief: Hack into the Squid Game Tug of War

You sit in front of your screen, the soft glow of code reflecting off your face in the dimly lit room. Time is ticking, and Player 48's life is hanging by a thread. The familiar hum of your custom-built terminal fills the air as you gain unauthorized access to the Squid Game’s player database. You know that the tug-of-war game is coming up fast, and Player 48 needs a perfect team to survive. They’re depending on you to find the best combination of strength, weight, and endurance. If you fail, Player 48 will be yanked into the abyss along with the rest of their team—game over, for good.

With a few swift keystrokes, the database opens up in front of you. Thousands of player profiles flicker by in an endless stream of numbers, stats, and personal data. But you don't have time for all of them. You need six players—just six—who can stand shoulder-to-shoulder with Player 48 and fight like their lives depend on it. And they do.

The game is rigged against them, but the right combination of 6 players could be the difference between victory and a deadly fall. As you scour the profiles, patterns emerge. Some players have immense strength, while others possess the weight needed to counterbalance the pull. And then there are those who can outlast any opponent in sheer endurance."""
    self.text_to_display2 = """        <h1>Mission Brief: Hack into the Squid Game Tug of War</h1>
        <p>You sit in front of your screen, the soft glow of code reflecting off your face in the dimly lit room. <span class="highlight">Time is ticking</span>, and Player 48's life is hanging by a thread. The familiar hum of your custom-built terminal fills the air as you gain unauthorized access to the Squid Game’s player database.</p>
        
        <p>You know that the tug-of-war game is coming up fast, and Player 48 needs a <span class="highlight">perfect team to survive</span>. They’re depending on you to find the best combination of strength, weight, and endurance. If you fail, Player 48 will be yanked into the abyss along with the rest of their team—game over, for good.</p>
        
        <p>With a few swift keystrokes, the database opens up in front of you. Thousands of player profiles flicker by in an endless stream of numbers, stats, and personal data. But you don't have time for all of them. <span class="highlight">You need six players—just six</span>—who can stand shoulder-to-shoulder with Player 48 and fight like their lives depend on it. And they do.</p>
        
        <p>The game is rigged against them, but the right combination of 6 players could be the difference between victory and a deadly fall. As you scour the profiles, patterns emerge. Some players have immense strength, while others possess the weight needed to counterbalance the pull. And then there are those who can outlast any opponent in sheer endurance.</p>
        <p>To start, click the buttons below to download the instructions and files needed to solve this puzzle.</p>
        """
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js("startTypingEffect", self.type_text)
    self.total_time = 0
    self.begin_time = False
    self.stay_alive = 0
    self.still.visible = False
    self.animated.visible = False
    self.sim_win.visible = False
    self.sim_fail.visible = False
    

  def type_text(self):
    # Remove cursor if it's there
    time.sleep(3)
    self.image_1.visible = False
    self.still.visible = True
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
      Timer.start_time('p4')
      # anvil.server.call_s('start_timer', 'p4_start')
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
    combination_value = self.combination_lock_1.get_combination()
    if HashingFunction.hash_func(combination_value) == 3989186883:
      self.animated.visible = True
      self.still.visible = False
      time.sleep(4)
      self.animated.visible = False
      self.sim_win.visible = True
      Notification(f"Team Positions Simulation Passed! Moving to next stage...").show()
      time.sleep(6)
      open_form('P5_Marbles')
    else:
      self.combination_lock_1.clear_values()
      self.combination_lock_1.flash_effect()
      self.animated.visible = True
      self.still.visible = False
      time.sleep(3)
      self.animated.visible = False
      self.sim_fail.visible = True
      time.sleep(5)
      Notification(f"Team Positions Simulation Failed! Try again...").show()
      time.sleep(1)
      self.still.visible = True
      self.sim_fail.visible = False
      
  def instruction_file_click(self, **event_args):
    '''
    file_media = anvil.server.call('get_file','p4_file')
    if file_media is not None:
      anvil.download(file_media)
    else:
      notification = "The file could not be found."
      anvil.alert(notification)
    '''
    anvil.js.window.open("https://colab.research.google.com/drive/1PxaJm5p-e3Vi2U6uairMdbMWkp9zgYA3?usp=sharing", "_blank")

