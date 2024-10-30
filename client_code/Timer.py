import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta, timezone
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#

current_time = 0

def get_time():
  return current_time

def set_time(time):
  global current_time
  current_time = time

team_times_start = {}
team_times_end = None
time_elapsed = None

def start_time(problem):
  global team_times_start
  team_times_start[problem] = datetime.now(timezone.utc)

def end_time():
  global team_times_end
  global time_elapsed
  team_times_end = datetime.now(timezone.utc)
  time_elapsed = (team_times_end - team_times_start['p1']).total_seconds()

  return int(time_elapsed)

team_name = None

def set_team_name(new_name):
  global team_name
  team_name = new_name

def commit_times():
  global team_times_start
  global team_times_end
  global time_elapsed
  global team_name
  team = app_tables.teams.get(team_name=team_name)

  for problem, start_time in team_times_start.items():
    problem_column = problem + "_start"
    team[problem_column] = start_time

  team['end'] = team_times_end
  team['total_time'] = time_elapsed

  

  
