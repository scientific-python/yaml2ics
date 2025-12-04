# Changelog for yaml2ics

## [v0.3](https://github.com/scientific-python/yaml2ics/tree/v0.3)

### Enhancements

- Print concise error messages when invoking `yaml2ics` command ([#55](https://github.com/scientific-python/yaml2ics/pull/55)).
- Default to UTC timezone ([#116](https://github.com/scientific-python/yaml2ics/pull/116)).

### Bug Fixes

- Unpin pytest ([#88](https://github.com/scientific-python/yaml2ics/pull/88)).
- BUG: include timezone info in datetime_to_str converter ([#115](https://github.com/scientific-python/yaml2ics/pull/115)).
- Correctly infer timezone from event begin time ([#125](https://github.com/scientific-python/yaml2ics/pull/125)).

### Maintenance

- Test on Python 3.12.0-beta.2 ([#56](https://github.com/scientific-python/yaml2ics/pull/56)).
- Use label-check and attach-next-milestone-action ([#58](https://github.com/scientific-python/yaml2ics/pull/58)).
- Use setuptools ([#59](https://github.com/scientific-python/yaml2ics/pull/59)).
- Specify what goes in sdist ([#60](https://github.com/scientific-python/yaml2ics/pull/60)).
- Use changelist ([#61](https://github.com/scientific-python/yaml2ics/pull/61)).
- Use dependabot ([#62](https://github.com/scientific-python/yaml2ics/pull/62)).
- Use trusted publisher ([#70](https://github.com/scientific-python/yaml2ics/pull/70)).
- Pin ics-vtimezones to 2020.1 ([#78](https://github.com/scientific-python/yaml2ics/pull/78)).
- Pin pytest ([#85](https://github.com/scientific-python/yaml2ics/pull/85)).
- Use setup-python pip caching ([#87](https://github.com/scientific-python/yaml2ics/pull/87)).
- Add changelist config ([#94](https://github.com/scientific-python/yaml2ics/pull/94)).
- Update pre-commit repos ([#95](https://github.com/scientific-python/yaml2ics/pull/95)).
- Update ruff config ([#96](https://github.com/scientific-python/yaml2ics/pull/96)).
- Update GH actions ([#97](https://github.com/scientific-python/yaml2ics/pull/97)).
- Add codespell pre-commit ([#98](https://github.com/scientific-python/yaml2ics/pull/98)).
- Test on Python 3.13-dev ([#99](https://github.com/scientific-python/yaml2ics/pull/99)).
- Fix cli and inclusion file tests ([#104](https://github.com/scientific-python/yaml2ics/pull/104)).
- Update pytest config ([#100](https://github.com/scientific-python/yaml2ics/pull/100)).
- Update pre-commit (12/2024) ([#107](https://github.com/scientific-python/yaml2ics/pull/107)).
- Support for Python: added 3.13, 3.14, removed 3.8 ([#119](https://github.com/scientific-python/yaml2ics/pull/119)).
- MAINT: actually bumping minimum python to 3.9 [#126](https://github.com/scientific-python/yaml2ics/pull/126)).

### Other

- CI: adding workflow_dispatch ([#84](https://github.com/scientific-python/yaml2ics/pull/84)).

### Contributors

3 authors added to this release (alphabetically):

- Brigitta Sipőcz ([@bsipocz](https://github.com/bsipocz))
- Jarrod Millman ([@jarrodmillman](https://github.com/jarrodmillman))
- Stefan van der Walt ([@stefanv](https://github.com/stefanv))

3 reviewers added to this release (alphabetically):

- Brigitta Sipőcz ([@bsipocz](https://github.com/bsipocz))
- Jarrod Millman ([@jarrodmillman](https://github.com/jarrodmillman))
- Stefan van der Walt ([@stefanv](https://github.com/stefanv))

## [v0.2](https://github.com/scientific-python/yaml2ics/tree/v0.2)

[Full Changelog](https://github.com/scientific-python/yaml2ics/compare/v0.1...v0.2)

**Merged pull requests:**

- Update pre-commit hooks [\#53](https://github.com/scientific-python/yaml2ics/pull/53) ([jarrodmillman](https://github.com/jarrodmillman))
- Update codecov [\#52](https://github.com/scientific-python/yaml2ics/pull/52) ([jarrodmillman](https://github.com/jarrodmillman))
- Update pre-commit [\#50](https://github.com/scientific-python/yaml2ics/pull/50) ([jarrodmillman](https://github.com/jarrodmillman))
- Increase coverage to 100% [\#48](https://github.com/scientific-python/yaml2ics/pull/48) ([stefanv](https://github.com/stefanv))
- Switch from flake8 to ruff [\#47](https://github.com/scientific-python/yaml2ics/pull/47) ([stefanv](https://github.com/stefanv))
- Flake8 migrated to GitHub [\#46](https://github.com/scientific-python/yaml2ics/pull/46) ([itrich](https://github.com/itrich))
- Add possibility to add additional dates to recurring events [\#45](https://github.com/scientific-python/yaml2ics/pull/45) ([itrich](https://github.com/itrich))

## [v0.1](https://github.com/scientific-python/yaml2ics/tree/v0.1)

[Full Changelog](https://github.com/scientific-python/yaml2ics/compare/v0.1rc3...v0.1)

**Closed issues:**

- Release please [\#42](https://github.com/scientific-python/yaml2ics/issues/42)

**Merged pull requests:**

- Announce Python 3.11 support [\#43](https://github.com/scientific-python/yaml2ics/pull/43) ([jarrodmillman](https://github.com/jarrodmillman))
- Add ability to specify custom ICS [\#41](https://github.com/scientific-python/yaml2ics/pull/41) ([stefanv](https://github.com/stefanv))
- Fix markdown syntax [\#40](https://github.com/scientific-python/yaml2ics/pull/40) ([jarrodmillman](https://github.com/jarrodmillman))
- Add test and coverage badges [\#39](https://github.com/scientific-python/yaml2ics/pull/39) ([jarrodmillman](https://github.com/jarrodmillman))
- Update install and release notes [\#38](https://github.com/scientific-python/yaml2ics/pull/38) ([jarrodmillman](https://github.com/jarrodmillman))
- Measure test coverage [\#37](https://github.com/scientific-python/yaml2ics/pull/37) ([jarrodmillman](https://github.com/jarrodmillman))
- Add classifiers [\#36](https://github.com/scientific-python/yaml2ics/pull/36) ([jarrodmillman](https://github.com/jarrodmillman))
- Lint toml [\#35](https://github.com/scientific-python/yaml2ics/pull/35) ([jarrodmillman](https://github.com/jarrodmillman))
- Fix linting [\#34](https://github.com/scientific-python/yaml2ics/pull/34) ([jarrodmillman](https://github.com/jarrodmillman))

## [v0.1rc3](https://github.com/scientific-python/yaml2ics/tree/v0.1rc3) (2022-08-21)

[Full Changelog](https://github.com/scientific-python/yaml2ics/compare/v0.1rc2...v0.1rc3)

**Merged pull requests:**

- Use ics pypi pre-release [\#33](https://github.com/scientific-python/yaml2ics/pull/33) ([jarrodmillman](https://github.com/jarrodmillman))

## [v0.1rc2](https://github.com/scientific-python/yaml2ics/tree/v0.1rc2) (2022-08-12)

[Full Changelog](https://github.com/scientific-python/yaml2ics/compare/v0.1rc1...v0.1rc2)

**Closed issues:**

- Add the possibility to skip dates for recurring events [\#23](https://github.com/scientific-python/yaml2ics/issues/23)

**Merged pull requests:**

- Add changelog [\#32](https://github.com/scientific-python/yaml2ics/pull/32) ([jarrodmillman](https://github.com/jarrodmillman))
- Add release process notes [\#31](https://github.com/scientific-python/yaml2ics/pull/31) ([jarrodmillman](https://github.com/jarrodmillman))
- Specify lower bounds on dependencies [\#30](https://github.com/scientific-python/yaml2ics/pull/30) ([jarrodmillman](https://github.com/jarrodmillman))
- Improve CI testing [\#29](https://github.com/scientific-python/yaml2ics/pull/29) ([jarrodmillman](https://github.com/jarrodmillman))
- Run linter [\#28](https://github.com/scientific-python/yaml2ics/pull/28) ([jarrodmillman](https://github.com/jarrodmillman))
- Update precommit hooks [\#27](https://github.com/scientific-python/yaml2ics/pull/27) ([jarrodmillman](https://github.com/jarrodmillman))
- Update GH actions [\#26](https://github.com/scientific-python/yaml2ics/pull/26) ([jarrodmillman](https://github.com/jarrodmillman))
- Simplify install [\#25](https://github.com/scientific-python/yaml2ics/pull/25) ([jarrodmillman](https://github.com/jarrodmillman))
- Add the possibility to skip dates for recurring events [\#24](https://github.com/scientific-python/yaml2ics/pull/24) ([itrich](https://github.com/itrich))
- yaml2ics: Allow a "timezone" option within each event. [\#22](https://github.com/scientific-python/yaml2ics/pull/22) ([rkdarst](https://github.com/rkdarst))

## [v0.1rc1](https://github.com/scientific-python/yaml2ics/tree/v0.1rc1) (2022-03-02)

[Full Changelog](https://github.com/scientific-python/yaml2ics/compare/v0.0...v0.1rc1)

**Implemented enhancements:**

- Add X-WR-CALNAME in extras on top of NAME [\#16](https://github.com/scientific-python/yaml2ics/pull/16) ([tupui](https://github.com/tupui))

**Closed issues:**

- Build system [\#20](https://github.com/scientific-python/yaml2ics/issues/20)
- Make installable? [\#17](https://github.com/scientific-python/yaml2ics/issues/17)
- Intervals between events is not respected [\#14](https://github.com/scientific-python/yaml2ics/issues/14)
- Updating to ICS 0.8 [\#3](https://github.com/scientific-python/yaml2ics/issues/3)
- Roadmap of this project [\#1](https://github.com/scientific-python/yaml2ics/issues/1)

**Merged pull requests:**

- Package library [\#19](https://github.com/scientific-python/yaml2ics/pull/19) ([tupui](https://github.com/tupui))
- Add missing interval to RRULE [\#15](https://github.com/scientific-python/yaml2ics/pull/15) ([stefanv](https://github.com/stefanv))
- Add calendar name field [\#13](https://github.com/scientific-python/yaml2ics/pull/13) ([stefanv](https://github.com/stefanv))
- Update black [\#12](https://github.com/scientific-python/yaml2ics/pull/12) ([stefanv](https://github.com/stefanv))
- Add 'include' to metadata to include other files. [\#11](https://github.com/scientific-python/yaml2ics/pull/11) ([rkdarst](https://github.com/rkdarst))
- Add Github Actions to run tests [\#10](https://github.com/scientific-python/yaml2ics/pull/10) ([rkdarst](https://github.com/rkdarst))
- Fix several tests [\#9](https://github.com/scientific-python/yaml2ics/pull/9) ([rkdarst](https://github.com/rkdarst))
- Add per-calendar default timezone \(in meta header\) [\#8](https://github.com/scientific-python/yaml2ics/pull/8) ([rkdarst](https://github.com/rkdarst))
- Don't set end=None for recurring events [\#7](https://github.com/scientific-python/yaml2ics/pull/7) ([rkdarst](https://github.com/rkdarst))
- Fix rrule creation: use name= and value= for more correct syntax. [\#6](https://github.com/scientific-python/yaml2ics/pull/6) ([rkdarst](https://github.com/rkdarst))
- Print error messages to stderr, not stdout [\#5](https://github.com/scientific-python/yaml2ics/pull/5) ([rkdarst](https://github.com/rkdarst))
- Port yaml2ics to ics 0.8.0 [\#4](https://github.com/scientific-python/yaml2ics/pull/4) ([rkdarst](https://github.com/rkdarst))
- requirements: Add PyYAML [\#2](https://github.com/scientific-python/yaml2ics/pull/2) ([rkdarst](https://github.com/rkdarst))

\* _This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)_
