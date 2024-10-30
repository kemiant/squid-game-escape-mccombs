from ._anvil_designer import P5_MarblesTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import Timer
import anvil.js
import time
from .. import Timer

class P5_Marbles(P5_MarblesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """Codebreaker: The Marble Gambit
You’re not in the arena, but the pressure still weighs heavy on your shoulders. Behind your screen, you're the last hope for a participant trapped in the deadly Squid Game. They've made it this far, but now it’s your turn to tip the scales in their favor—or let them fall. The next challenge is ruthless: you must solve at least 10 coding problems to secure 10 marbles. Without them, their time in the game is over.

The rules are clear, but the task is anything but easy. Every problem you solve earns you 1 marble. You need 10 marbles to unlock the path to the next stage and save the participant. The timer in the corner ticks down, a constant reminder that failure is not an option.

30 questions flood your screen, each more complex than the last. For every answer you submit, every line of code you crack, a marble edges closer to your grasp. But time is running out. It’s a race against the clock, a battle of wits, and the weight of someone’s fate is on your shoulders.

Will you gather the 10 marbles in time, or will the participant’s journey end here—because of you?"""
    self.text_to_display2 = """<h2>Codebreaker: The Marble Gambit</h2>

<p>You’re not in the arena, but the pressure still weighs heavy on your shoulders. Behind your screen, you're the last hope for a participant trapped in the deadly Squid Game. They've made it this far, but now it’s your turn to tip the scales in their favor—or let them fall. The next challenge is ruthless: you must solve at least <strong>10 coding problems</strong> to secure <strong>10 marbles</strong>. Without them, their time in the game is over.</p>

<p>The rules are clear, but the task is anything but easy. Every problem you solve earns you <strong>1 marble</strong>. You need <strong>10 marbles</strong> to unlock the path to the next stage and save the participant. The timer in the corner ticks down, a constant reminder that failure is not an option.</p>

<p>30 questions flood your screen, each more complex than the last. For every answer you submit, every line of code you crack, a marble edges closer to your grasp. But time is running out. It’s a race against the clock, a battle of wits, and the weight of someone’s fate is on your shoulders. You will need to download and use the Games.csv and Rounds.csv table to solve these questions.</p>

<p><strong>Will you gather the 10 marbles in time, or will the participant’s journey end here—because of you?</strong></p>
"""
    self.animated.visible =False
    self.still.visible =True
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js("startTypingEffect", self.type_text)
    self.total_time = 0
    self.begin_time = False
    self.stay_alive = 0
    self.questions = [
        {"question": "Find the game with the highest survival rate.", "item_index": i} for i, q in enumerate([
          "Find the game with the highest survival rate.",
          "List all games where the survival rate is above 50%. (Count)",
          "How many games have a difficulty rating of 8 or higher?",
          "Display the count of games where the maximum participants exceed 100.",
          "Find the game with the lowest difficulty level.",
          "What is the average survival rate across all games?",
          "How many games have exactly 100 participants?",
          "Retrieve the game with the lowest difficulty.",
          "Find the count of games with a survival rate less than 0.5.",
          "Count how many games have a survival rate of exactly 50%.",
          "Which game has the fewest participants?",
          "Calculate the total number of participants across all games.",
          "Find the difference in difficulty between the hardest and easiest game.",
          "How many games have a difficulty rating of 7?",
          "Retrieve the game where the survival rate is lower than 0.4.",
          "Find the round with the highest number of eliminations.",
          "How many rounds had more than 20 eliminations?",
          "How many rounds from game with GameID = 4?",
          "What is the total number of survivors in all rounds?",
          "How many rounds have exactly 1 survivor?",
          "How many rounds occurred in January 2024?",
          "How many rounds had fewer than 10 survivors?",
          "How many rounds had fewer eliminations than survivors?",
          "How many unique games are present in the rounds dataset?",
          "What is the highest number of survivors in any round?",
          "What is the average number of eliminations per round?",
          "How many rounds had exactly 1 elimination?",
          "Which round had the smallest number of survivors?",
          "How many rounds had at least 50 eliminations?",
          "What is the highest number of eliminations in a round?"
        ])
    ]

    self.repeating_panel_1.items = self.questions
    self.correct_answers = [
      "Honeycomb/Dalgona",  # Answer to question 1
      "1",  # Answer to question 2
      "3",  # Answer to question 3
      "2",  # Answer to question 4
      "Marbles",  # Answer to question 5
      "0.45",  # Answer to question 6
      "1",  # Answer to question 7
      "Marbles",  # Answer to question 8
      "3",  # Answer to question 9
      "2",  # Answer to question 10
      "Glass Bridge",  # Answer to question 11
      "840",  # Answer to question 12
      "4",  # Answer to question 13
      "1",  # Answer to question 14
      "Glass Bridge",  # Answer to question 15
      "20",  # Answer to question 16
      "0",  # Answer to question 17
      "2",  # Answer to question 18
      "43",  # Answer to question 19
      "1",  # Answer to question 20
      "5",  # Answer to question 21
      "3",  # Answer to question 22
      "0",  # Answer to question 23
      "3",  # Answer to question 24
      "20",  # Answer to question 25
      "8.6",  # Answer to question 26
      "4",  # Answer to question 27
      "1",  # Answer to question 28
      "0",  # Answer to question 29
      "20"]  # Answer to question 30
    self.correct_count = 0
    self.marble_counter.text = f"{self.correct_count} out of 10"
    self.card_2.visible =False
    self.card_3.visible =False
    self.grid_panel_1.visible =False

    # Function to store answers from the repeating panel

  
  def store_answer(self, question_index, answer):
    # Check if the answer is correct by comparing it to the correct answer
    correct_answer = self.correct_answers[question_index]
    
    if answer == correct_answer:
      self.correct_count += 1
      Notification(f"Correct!").show()
      self.animated.visible =True
      self.still.visible =False
    else:
      Notification(f"Incorrect.").show()
    
    # Update the correct count label
    self.marble_counter.text = f"{self.correct_count} out of 10"
        # Check if the marble counter equals 10
    if self.correct_count == 10:
      Notification("You've earned 10 marbles! You may proceed alive...").show()
      time.sleep(2)
      open_form('P6_Old_Man_1')  # Replace 'form_4' with the actual form name

  def update_item_index(self, current_index, new_index):
    # Find the item in the questions list and update the item_index
    for question in self.questions:
      if question['item_index'] == current_index:
        question['item_index'] = new_index
        break
    
    # Optionally, refresh the repeating panel if needed
    self.repeating_panel_1.items = self.questions

  
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
      self.grid_panel_1.visible =True
      Timer.start_time('p5')
      # anvil.server.call_s('start_timer', 'p5_start')
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

  


  