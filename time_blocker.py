import os
import json
import datetime
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from apiclient.discovery import build
from httplib2 import Http

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

def print_banner():
    banner = """
    ============================================
       Automated Time Blocking Tool 
    Manage your time effectively using this tool.
    ============================================
    """
    print(banner)

def authenticate_google_account():
    store = Storage(TOKEN_FILE)
    creds = store.get()
    
    if not creds or creds.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        creds = run_flow(flow, store)
    
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service

def get_calendar_events(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('Fetching upcoming events...')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
        return []
    return events

def add_time_block_event(service, start_time, end_time, summary):
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_time,
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'UTC',
        },
    }
    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print('Created event: {}'.format(created_event.get('htmlLink')))

def auto_time_block(service):
    events = get_calendar_events(service)
    
    for event in events:
        start_time = event['start'].get('dateTime', event['start'].get('date'))
        end_time = event['end'].get('dateTime', event['end'].get('date'))
        
        print('Existing event: {}'.format(event.get('summary')))
        print('Start: {}, End: {}'.format(start_time, end_time))
        
        start_dt = datetime.datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ') + datetime.timedelta(hours=1)
        end_dt = start_dt + datetime.timedelta(hours=1)
        
        start_str = start_dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        end_str = end_dt.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        
        add_time_block_event(service, start_str, end_str, 'Work Block - Focused Time')

def main():
    print_banner()
    service = authenticate_google_account()
    auto_time_block(service)

if __name__ == '__main__':
    main()
