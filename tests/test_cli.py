import datetime
import io
import os
import zoneinfo

import pytest

from yaml2ics import event_from_yaml, files_to_events, main

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
example_calendar = os.path.join(basedir, "../example/test_calendar.yaml")


def test_cli():
    main(["yaml2ics.py", example_calendar])

    with pytest.raises(RuntimeError) as e:
        main(["yaml2ics.py"])
        assert "Usage:" in str(e)

    with pytest.raises(RuntimeError) as e:
        main(["yaml2ics.py", "syzygy.yaml"])
        assert "is not a file" in str(e)


def test_errors():
    begin = datetime.date(2025, 12, 1)
    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"begin": begin, "repeat": {"interval": {}}})
    assert "interval must specify" in str(e)

    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"begin": begin, "ics": "123"})
    assert "Invalid custom ICS" in str(e)

    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"begin": begin, "repeat": {"interval": {"weeks": 1}}})
    assert "must specify end date for repeating events" in str(e)

    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"begin": begin, "repeat": {"interval": {"epochs": 4}}})
    assert "expected interval to be specified in seconds, minutes" in str(e)


def test_invalid_timezone():
    f = io.BytesIO(b"""
    name: Invalid tz cal
    timezone: US/Pacificana
     """)
    with pytest.raises(zoneinfo.ZoneInfoNotFoundError):
        files_to_events([f])
