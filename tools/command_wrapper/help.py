"""Parse the flag types Maya help can describe; require overrides for the rest."""

import re


def command_flags(
    command: str, help_text: str, overrides: dict[str, str]
) -> dict[str, str]:
    types = {
        "": "bool",
        "String": "str",
        "Int": "int",
        "Float": "float",
        "Boolean": "bool",
        "Length": "float",
        "on|off": "bool",
    }
    flags: dict[str, str] = {}
    for line in help_text.splitlines():
        if not line.lstrip().startswith("-"):
            continue
        match = re.fullmatch(r"\s*-(\w+)\s+-(\w+)\s*(.*?)\s*", line)
        if match is None:
            raise ValueError(f"{command}: unsupported flag help line {line!r}")
        alias, name, maya_type = match.groups()
        annotation = overrides.get(name, overrides.get(alias, types.get(maya_type)))
        if annotation is None:
            raise ValueError(
                f"{command}.{name}: unsupported help type {maya_type!r}; "
                "supply a flag_type_overrides entry"
            )
        flags[name] = annotation
        flags[alias] = annotation
    if not flags and not overrides:
        raise ValueError(
            f"{command}: no flags found in Maya help; supply flag_type_overrides"
        )
    flags.update(overrides)
    return flags
