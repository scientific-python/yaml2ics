import textwrap

import yaml


def parse_yaml(yaml_str):
    return yaml.load(textwrap.dedent(yaml_str).strip(), Loader=yaml.FullLoader)
