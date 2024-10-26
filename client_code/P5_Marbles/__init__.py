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

class P5_Marbles(P5_MarblesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_to_display1 = """Using the games and rounds dataset"""
    self.text_to_display2 = """"""
    # Counter for the position of next character to display
    self.current_position = 0
    # Start the typing effect
    anvil.js.call_js("startTypingEffect", self.type_text)
    self.total_time = 0
    self.begin_time = False
    self.stay_alive = 0
    questions_dict = {
      "question": "Find the game with the highest survival rate.",
      "question": "List all games where the survival rate is above 50%. (Count)",
      "question": "How many games have a difficulty rating of 8 or higher?",
      "question": "Display the count of games where the maximum participants exceed 100.",
      "question": "Find the game with the lowest difficulty level.",
      "question": "What is the average survival rate across all games?",
      "question": "How many games have exactly 100 participants?",
      "question": "Retrieve the game with the lowest difficulty.",
      "question": "Find the count of games with a survival rate less than 0.5.",
      "question": "Count how many games have a survival rate of exactly 50%.",
      "question": "Which game has the fewest participants?",
      "question": "Calculate the total number of participants across all games.",
      "question": "Find the difference in difficulty between the hardest and easiest game.",
      "question": "How many games have a difficulty rating of 7?",
      "question": "Retrieve the game where the survival rate is lower than 0.4.",
      "question": "Find the round with the highest number of eliminations.",
      "question": "How many rounds had more than 20 eliminations?",
      "question": "How many rounds from game with GameID = 4?",
      "question": "What is the total number of survivors in all rounds?",
      "question": "How many rounds have exactly 1 survivor?",
      "question": "How many rounds occurred in January 2024?",
      "question": "How many rounds had fewer than 10 survivors?",
      "question": "How many rounds had fewer eliminations than survivors?",
      "question": "How many unique games are present in the rounds dataset?",
      "question": "What is the highest number of survivors in any round?",
      "question": "What is the average number of eliminations per round?",
      "question": "How many rounds had exactly 1 elimination?",
      "question": "Which round had the smallest number of survivors?",
      "question": "How many rounds had at least 50 eliminations?",
      "question": "What is the highest number of eliminations in a round?"}
    self.repeating_panel_1.items = self.questions
    answers_list = [
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


    # Function to store answers from the repeating panel

  
  def store_answer(self, question_index, answer):
    # Check if the answer is correct by comparing it to the correct answer
    correct_answer = self.correct_answers[question_index]
    
    if answer == correct_answer:
      self.correct_count += 1
      Notification(f"Correct!").show()
    else:
      Notification(f"Incorrect.").show()
    
    # Update the correct count label
    self.label_correct_count.text = f"Correct Answers: {self.correct_count}"
    
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
      anvil.server.call_s('start_timer', 'p5_start')
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
    combination_value = self.combination_lock_form.get_combination()
    if anvil.server.call_s("", combination_value):
      open_form("")

  def csv_file_click(self, **event_args):
    file_media = anvil.server.call('get_file','Games_CSV')
    if file_media is not None:
      anvil.download(file_media)
      #if need to download more put here
      file_media = anvil.server.call('get_file','rounds_csv')
      anvil.download(file_media)
    else:
      notification = "The file could not be found."
      anvil.alert(notification)


  def db_file_click(self, **event_args):
    file_media = anvil.server.call('get_file','sqlite_all_files')
    if file_media is not None:
      anvil.download(file_media)
    else:
      notification = "The file could not be found."
      anvil.alert(notification)