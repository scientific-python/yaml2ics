import io
import textwrap

from util import parse_yaml

from yaml2ics import events_to_calendar, files_to_calendar


def test_calendar_structure():
    cal = events_to_calendar([])
    cal_str = cal.serialize()
    assert cal_str.startswith('BEGIN:VCALENDAR')
    assert cal_str.endswith('END:VCALENDAR')

def test_calendar_event():
    cal = files_to_calendar(
        [io.StringIO(textwrap.dedent(
            '''
            events:
              - summary: Earth Day
                begin: 2021-04-22
                url: https://earthday.org
                location: Earth
            '''
        ))]
    )
    cal_str = cal.serialize()
    assert cal_str.startswith('BEGIN:VCALENDAR')
    assert 'SUMMARY:Earth Day' in cal_str
    assert cal_str.endswith('END:VCALENDAR')
