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

team_times_start = {'p1':None, 'p2':None, 'p3':None, 'p4':None, 'p5':None,'p6': None, 'end': None}
team_times_end = None
time_elapsed = None

def start_time(problem):
  global team_times_start
  team_times_start[problem] = datetime.now(timezone.utc)

def end_time():
  global team_times_end
  global time_elapsed
  global team_times_start
  team_times_start['end'] = datetime.now(timezone.utc)
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


def start_resume_team():
  global team_times_start
  global team_name
  team = app_tables.teams.get(team_name=team_name)
  last_question = 'p1'

  if team:
    challenge_map = {
            'p1_start': 'P1_Red_Light',
            'p2_start': 'P2_Glass_Steps',
            'p3_start': 'P3_Sugar_Cookies',
            'p4_start': 'P4_Tug_War',
            'p5_start': 'P5_Marbles',
            'p6_start': 'P6_Old_Man_1',
            'end_start': 'Completion'
        }
    
    for problem, time in team_times_start.items():
      if time:
        last_question = problem
      else:
        break
    last_form = challenge_map[last_question + '_start']
    return {'status': 'resumed', 'last_started_form': last_form}
  
  else:
    app_tables.teams.add_row(
            team_name=team_name, 
            total_time=None, 
            p1_start=None,
            p2_start=None,
            p3_start=None,
            p4_start=None,
            p5_start=None,
            p6_start=None,
            end=None
        )
    # anvil.server.session['team_name'] = team_name
    return {
        'status': 'registered'
    }
