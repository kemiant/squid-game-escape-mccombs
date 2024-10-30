from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Bind the repeating panel data (display the question)
    self.label_1.text = self.item['question']
    # Any code you write here will run before the form opens.

  def button_click(self, **event_args):
    """This method is called when the user clicks the Submit button for each question"""
    # Retrieve the answer from the textbox
    answer = self.text_box_1.text
    
    # Send the answer to the main form for storage and correctness check
   # if self.item['item_index'] != -1:
    get_open_form().store_answer(self.item['item_index'], answer)
      #update_item_index(self.item['item_index'], -1)
      #get_open_form().update_item_index(self.item['item_index'], -1)

  def text_box_1_focus(self, **event_args):
    # Check if the text is still the default text
    if self.text_box_1.text == "Type your answer here...":
      # Clear the default text
      self.text_box_1.text = ""
      
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
    
