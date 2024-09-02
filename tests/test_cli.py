import os

import pytest

from yaml2ics import event_from_yaml, main

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
    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"repeat": {"interval": {}}})
    assert "interval must specify" in str(e)

    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"ics": "123"})
    assert "Invalid custom ICS" in str(e)

    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"repeat": {"interval": {"weeks": 1}}})
    assert "must specify end date for repeating events" in str(e)

    with pytest.raises(RuntimeError) as e:
        event_from_yaml({"repeat": {"interval": {"epochs": 4}}})
    assert "expected interval to be specified in seconds, minutes" in str(e)
