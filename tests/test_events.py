from util import parse_yaml

from yaml2ics import event_ics_from_yaml


def test_basic_structure():
    event = event_ics_from_yaml(
        parse_yaml(
            '''
            name: Earth Day
            begin: 2021-04-22
            url: https://earthday.org
            '''
        )
    )

    # All lines must be separated by CRLF
    lines = event.split('\n')
    for line in lines[:-1]:
        assert line.endswith('\r')

    # All events must have a DTSTAMP
    assert 'DTSTAMP' in event


def test_all_day_event():
    event = event_ics_from_yaml(
        parse_yaml(
            '''
            name: Earth Day
            begin: 2021-04-22
            url: https://earthday.org
            '''
        )
    )
    assert event.startswith('BEGIN:VEVENT')
    assert event.endswith('END:VEVENT')
    assert 'DTSTART;VALUE=DATE:20210422' in event
    assert 'DTEND' not in event


def test_rrule():
    event = event_ics_from_yaml(
        parse_yaml(
            '''
            name: Earth Day
            begin: 2021-04-22
            url: https://earthday.org
            repeat:
              interval:
                years: 1
              until: 2030-04-22
            '''
        )
    )
    assert 'DTEND' not in event
    assert 'RRULE:FREQ=YEARLY;UNTIL=20300422T000000Z' in event


def test_event_with_time_range():
    event = event_ics_from_yaml(
        parse_yaml(
            '''
            name: Event of the Century
            begin: 2021-09-21 15:00-07:00
            end: 2021-09-21 15:30:00-07:00
            description: |
              Meet the team on the northern side of the field.
            '''
        )
    )
    assert 'DTSTART' in event
    assert 'DTEND' in event


def test_event_with_duration():
    event = event_ics_from_yaml(
        parse_yaml(
            '''
            name: Event of the Century
            begin: 2021-09-21 15:00-07:00
            duration:
              minutes: 30
            description: |
              Meet the team on the northern side of the field.
            '''
        )
    )

    assert 'DURATION:PT30M' in event
    assert 'DTEND' not in event
    assert 'DTSTART' in event
