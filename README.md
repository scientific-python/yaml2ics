# YAML to iCalendar (ics)

Please see `example/test_calendar.yaml` for example entries.

To produce a calendar from a list of events:

```
python yaml2ics.py example/test_calendar.yaml
```

To combine lists of events in to a calendar:

```
python yaml2ics.py example/test_calendar.yaml example/another_calendar.yaml
```

To test:

```
PYTHONPATH=. pytest
```
