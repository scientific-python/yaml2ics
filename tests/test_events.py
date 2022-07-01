from util import parse_yaml

from yaml2ics import event_from_yaml


def test_basic_structure():
    event = event_from_yaml(
        parse_yaml(
            """
            summary: Earth Day
            begin: 2021-04-22
            url: https://earthday.org
            location: Earth
            """
        )
    )

    # All lines must be separated by CRLF
    event_str = event.serialize()
    lines = event_str.split("\n")
    for line in lines[:-1]:
        assert line.endswith("\r")
    assert "SUMMARY:Earth Day" in event_str
    assert "URL:https://earthday.org" in event_str
    assert "LOCATION:Earth" in event_str
    # All events must have a DTSTAMP
    assert "DTSTAMP" in event_str


def test_all_day_event():
    event = event_from_yaml(
        parse_yaml(
            """
            summary: Earth Day
            begin: 2021-04-22
            url: https://earthday.org
            """
        )
    )
    event_str = event.serialize()
    assert event_str.startswith("BEGIN:VEVENT")
    assert event_str.endswith("END:VEVENT")
    assert "DTSTART;VALUE=DATE:20210422" in event_str
    # ics 0.8.0 does have DTEND that is the next day.
    # assert 'DTEND' not in event_str


def test_rrule():
    event = event_from_yaml(
        parse_yaml(
            """
            summary: Earth Day
            begin: 2021-04-22
            url: https://earthday.org
            repeat:
              interval:
                years: 1
              until: 2030-04-22
            """
        )
    )
    event_str = event.serialize()
    # DTEND exists and is the next day, calendar tools import this
    # correctly as being a one-day event
    assert "RRULE:FREQ=YEARLY;UNTIL=20300422T000000" in event_str


def test_exception():
    event = event_from_yaml(
        parse_yaml(
            """
            summary: Recurring event with exception
            timezone: America/Los_Angeles
            begin: 2022-07-01 10:00:00
            duration: {minutes: 60}
            repeat:
              interval:
                hours: 4
              until: 2022-07-31
              except_on:
                - 2022-07-13
                - 2022-07-14 06:00:00
            """
        )
    )
    event_str = event.serialize()
    # DTEND exists and is the next day, calendar tools import this
    # correctly as being a one-day event
    assert (
        "EXDATE;TZID=/ics.py/2020.1/America/Los_Angeles:20220713,20220714T060000"
        in event_str
    )


def test_event_with_time_range():
    event = event_from_yaml(
        parse_yaml(
            """
            summary: Event of the Century
            begin: 2021-09-21 15:00:00 -07:00
            end: 2021-09-21 15:30:00 -07:00
            description: |
              Meet the team on the northern side of the field.
            """
        )
    )
    event_str = event.serialize()
    assert "DTSTART" in event_str
    assert "DTEND" in event_str


def test_event_with_duration():
    event = event_from_yaml(
        parse_yaml(
            """
            summary: Event of the Century
            begin: 2021-09-21 15:00:00 -07:00
            duration:
              minutes: 30
            description: |
              Meet the team on the northern side of the field.
            """
        )
    )
    event_str = event.serialize()
    assert "DURATION:PT30M" in event_str
    assert "DTEND" not in event_str
    assert "DTSTART" in event_str
