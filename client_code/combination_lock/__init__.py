from ._anvil_designer import combination_lockTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class combination_lock(combination_lockTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def digit1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if len(self.digit1.text) > 2:
      self.digit1.text = self.digit1.text[2]
    if len(self.digit1.text) == 2:
      self.digit2.focus()

  def digit2_change(self, **event_args):
    if len(self.digit2.text) > 2:
      self.digit2.text = self.digit2.text[2]
    if len(self.digit2.text) == 2:
      self.digit3.focus()

  def digit3_change(self, **event_args):
    if len(self.digit3.text) > 2:
      self.digit3.text = self.digit3.text[2]
    if len(self.digit3.text) == 2:
      self.digit4.focus()

  def digit4_change(self, **event_args):
    if len(self.digit4.text) > 2:
      self.digit4.text = self.digit4.text[2]
    if len(self.digit4.text) == 2:
      self.digit5.focus()

  def digit5_change(self, **event_args):
    if len(self.digit5.text) > 2:
      self.digit5.text = self.digit5.text[2]
    if len(self.digit5.text) == 2:
      self.digit6.focus()

  def digit6_change(self, **event_args):
    if len(self.digit6.text) > 2:
      self.digit6.text = self.digit6.text[2]

  def get_combination(self):
    return ''.join([self.digit1.text, self.digit2.text, self.digit3.text, self.digit4.text, self.digit5.text, self.digit6.text])

  def clear_values(self):
        # Assuming digit1, digit2, ..., digit6 are the TextBox component names
        self.digit1.text = ''
        self.digit2.text = ''
        self.digit3.text = ''
        self.digit4.text = ''
        self.digit5.text = ''
        self.digit6.text = ''

  def flash_effect(self):
    anvil.js.call_js('flashUnderlineColorByClass', 'anvil-role-combination-lock', 3000)

