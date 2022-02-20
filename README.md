# YAML to iCalendar (ics)

Convert YAML files to .ics files which can be imported into other
calendar applications.

Features include:
- Converting single .yaml files, or combining multiple into one .ics
  file.
- ics fields: summary, description, location
- Specify event start+end or start+duration
- Recurring events (basic support)
- All-day events
- Timezone specification (default or per-event)



## Installation

There is no PyPI installation yet.  Requirements are in
`requirements.txt` and `yaml2ics.py` is a stand-alone script.



## Usage

To produce a calendar from a list of events:

```
python yaml2ics.py example/test_calendar.yaml
```

To combine lists of events in to a calendar:

```
python yaml2ics.py example/test_calendar.yaml example/another_calendar.yaml
```



## Syntax

Please see `example/test_calendar.yaml` for a full demo including
explanations.  Below is a minimal template that shows the basic idea:

```yaml
name: Calendar Name
timezone: Europe/Helsinki      # default timezoene for events, optional

events:
  - summary: The event title
    begin: 2021-09-21 15:00:00
    duration:
	  minutes: 30
    location: |
      https://meet.jit.si/example
    description: |
	  In this meeting we will ...
```



## Contributing

``requirements.dev.txt` contains the development requirements.

To test:

```
PYTHONPATH=. pytest
```

[black](https://github.com/psf/black) is used to auto-format files
(and enforced by CI).  To install git hooks, use `pre-commit install`.
To run the tests/auto-formatting manually, use `pre-commit run
--all-files`.



## Development status

Contributions welcome.

Currently alpha or beta: it works and is used, but mostly used by
those who contribute to it.  Expect bugs to still be found (and for
the best response, you probably want to dig into the problem to give
us a starting point).



## See also

* https://github.com/priyeshpatel/yaml-to-ical - older (~2014) idea of
  the same thing
