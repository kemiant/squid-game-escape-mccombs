import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
def hash_func(input_string):
    hash_value = 0
    for char in input_string:
        # Update the hash value by left-shifting and adding the character code
        hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF  # Limits to 32-bit integer
    return hash_value

def say_hello():
  print("Hello, world")
