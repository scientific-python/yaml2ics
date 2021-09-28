from yaml2ics import events_to_calendar_ics


def test_calendar_structure():
    cal = events_to_calendar_ics([])
    assert cal.startswith('BEGIN:VCALENDAR')
    assert cal.endswith('END:VCALENDAR')
