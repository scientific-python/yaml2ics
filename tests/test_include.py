import io
import os
import textwrap

from yaml2ics import files_to_calendar


def _read(f, mode=None):
    f = os.path.relpath(f)  # Changes ./a.yaml to a.yaml
    if f == "a.yaml":
        return io.StringIO(
            textwrap.dedent(
                """
            name: NAME123
            include:
             - b.yaml
             - c.yaml
            events:
              - summary: AAAAA
                begin: 2021-04-22
            """
            )
        )
    if f == "b.yaml":
        return io.StringIO(
            textwrap.dedent(
                """
            include:
             - d.yaml
            events:
              - summary: BBBBB
                begin: 2021-04-22
            """
            )
        )
    elif f in ("c.yaml", "d.yaml"):
        # Return template with summary of the letters
        return io.StringIO(
            textwrap.dedent(
                """
            events:
              - summary: %s
                begin: 2021-04-22
            """
                % (f[0].upper() * 5)
            )
        )
    else:
        raise RuntimeError("Attempting to load invalid test file")


def test_include_calendars(monkeypatch):
    """Calendar that includes other calendars"""
    monkeypatch.setitem(__builtins__, "open", _read)
    monkeypatch.setattr(os.path, "dirname", lambda _: ".")
    test_files = ["a.yaml", "b.yaml", "c.yaml", "d.yaml"]
    monkeypatch.setattr(os.path, "exists", lambda f: os.path.relpath(f) in test_files)
    cal = files_to_calendar(["a.yaml"])
    cal_str = cal.serialize()
    assert cal_str.startswith("BEGIN:VCALENDAR")
    assert "AAAAA" in cal_str
    assert "BBBBB" in cal_str
    assert "CCCCC" in cal_str
    assert "DDDDD" in cal_str
    assert "NAME:NAME123" in cal_str
    assert cal_str.endswith("END:VCALENDAR")
