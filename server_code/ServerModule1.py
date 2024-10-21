import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
import anvil.http
import requests
from datetime import datetime, timedelta, timezone
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def register_or_resume_team(team_name):
    team = app_tables.teams.get(team_name=team_name)
    
    if team:
        # Updated mapping of table column names to their corresponding form names
        challenge_map = {
            'c1_start': 'C1_IdentifyArt',
            'c2_start': 'C2_Blueprints',
            'c2_2_start': 'C2_P2_Adjust',
            'c2_3_start': 'C2_P3_Name',
            'c3_start': 'C3_Hacking',
            'c4_start': 'C4_Final',
            'end': 'Completion'
        }
        
        last_form = None
        last_time = None
        for col, form_name in challenge_map.items():
            start_time = team[col]
            if start_time is not None and (last_time is None or start_time > last_time):
                last_time = start_time
                last_form = form_name

        anvil.server.session['team_name'] = team_name
        return {
            'status': 'resumed',
            'last_started_form': last_form  # Return the form name for the latest challenge started
        }
    else:
        # Registering a new team if it doesn't exist
        app_tables.teams.add_row(
            team_name=team_name, 
            total_time=None, 
            c1_start=None,
            c2_start=None,
            c2_2_start=None,
            c2_3_start=None,
            c3_start=None,
            c4_start=None,
            end=None
        )
        anvil.server.session['team_name'] = team_name
        return {
            'status': 'registered'
        }



@anvil.server.callable
def start_timer(challenge):
    team_name = None
    if team_name is None:
        team_name = anvil.server.session.get('team_name', None)
    team = app_tables.teams.get(team_name=team_name)
    if team:
        team[challenge] = datetime.now(timezone.utc)

@anvil.server.callable
def stop_timer(team_name=None):
    if team_name is None:
      team_name = anvil.server.session.get('team_name', None)
    team = app_tables.teams.get(team_name=team_name)
    if team:
      elapsed_time = (datetime.now(timezone.utc) - team['c1_start']).total_seconds()
      team['total_time'] = elapsed_time
      team['end'] = datetime.now(timezone.utc)
      return elapsed_time
    return 0

#for setting timers
@anvil.server.callable
def get_elapsed_time(team_name=None):
    if team_name is None:
        team_name = anvil.server.session.get('team_name', None)
    team = app_tables.teams.get(team_name=team_name)
    if team and team['c1_start']:
        elapsed_time = (datetime.now(timezone.utc) - team['c1_start']).total_seconds()
        return int(elapsed_time)
    return 0