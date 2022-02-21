![PyPI](https://img.shields.io/pypi/v/yaml2ics?style=for-the-badge)

# YAML to iCalendar (ics)

Convert YAML files to .ics files which can be imported into other
calendar applications.

Features include:
- Converting single .yaml files, or combining multiple into one .ics
  file.
- ics fields: name, summary, description, location, timezone, repeat
- Specify event start+end or start+duration
- Recurring events (basic support)
- All-day events
- Timezone specification (default or per-event)

## Installation

```
pip install yaml2ics
```

**Note:** due to a pending release of a dependency (`ics-py`), an additional
step is required:

```
pip install -r requirements.txt
```

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
timezone: Europe/Helsinki  # default timezoene for events, optional

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

Contributions are welcomed! This project is still in active development
and should be considered beta.

[flit](https://flit.readthedocs.io/en/latest/) is used to manage the project.

```
pip install flit
pip install -r requirements.txt  # temporary workaround for ics-py
flit install -s  # make an editable/inplace installation
```

To test:

```
pytest
```

[black](https://github.com/psf/black) and other linters are used to auto-format
files (and enforced by CI). To install the git hooks, use `pre-commit install`.
To run the tests/auto-formatting manually, use `pre-commit run
--all-files`.

## See also

* https://github.com/priyeshpatel/yaml-to-ical - older (~2014) idea of
  the same thing
