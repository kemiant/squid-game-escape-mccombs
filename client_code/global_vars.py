import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import hashlib
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

total_time = 0

def say_hello():
  print("Hello, world")


def find_hash(password):
    hash_object = hashlib.sha256(password.encode()).hexdigest()
    return hash_object