from datetime import timedelta
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar

GMAIL = 'debroucker.tommy1@gmail.com'
PATH_JSON = 'cred_tommy.json'
CAL = GoogleCalendar(GMAIL, credentials_path=PATH_JSON)

def add_event(name, begin):
    event = Event(
        summary=name,
        start=begin,
        end=begin + timedelta(minutes=60),
        color_id=2
    )
    CAL.add_event(event)

def delete_all_event_permis():
    for e in CAL :
        if 'Place O Permis' in e.summary :
            CAL.delete_event(e)
