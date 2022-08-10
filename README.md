![PyPI](https://img.shields.io/pypi/v/yaml2ics?style=for-the-badge)

# YAML to iCalendar (ics)

| WARNING: this project is still in beta. Beware of breaking changes! |
| ------------------------------------------------------------------- |

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
explanations. Below is a minimal template that shows the basic idea:

```yaml
name: Calendar Name
timezone: Europe/Helsinki # default timezone for events, optional

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

To install the development version, fork the source of the project and make an
editable install:

```
pip install -e ".[test]"
```

To test:

```
pytest
```

[black](https://github.com/psf/black) and other linters are used to auto-format
files (and enforced by CI). To install the git hooks, use `pre-commit install`.
To run the tests/auto-formatting manually, use `pre-commit run --all-files`.

Releases are automatically pushed on PyPi by the CI when pushing a tag
following `*.*`.
