from tools.command_wrapper.metadata import ModeSignature
from tools.command_wrapper.modes import render_overload, render_typed_dict


def generate_mode_overloads(
    command: str,
    policy: ModeSignature,
    flags: dict[str, str],
    creation_flags: dict[str, str],
) -> str:
    if flags.keys() != creation_flags.keys():
        raise ValueError(f"{command}: creation and mode flags must match")
    unknown = set(policy.presence_flags) - flags.keys()
    if unknown:
        raise ValueError(f"{command}: unknown presence flags {unknown}")

    prefix = "_" + command[0].upper() + command[1:]
    common_name = f"{prefix}Flags"
    create_name = f"{prefix}CreateFlags"
    mode_name = f"{prefix}ModeFlags"
    mode_fields = {
        flag: annotation
        for flag, annotation in flags.items()
        if flag not in policy.presence_flags
    }
    create_fields = {
        flag: "Literal[False]" if flag in {"edit", "e", "query", "q"} else annotation
        for flag, annotation in creation_flags.items()
        if flag not in policy.presence_flags
    }
    common = {
        flag: annotation
        for flag, annotation in create_fields.items()
        if mode_fields[flag] == annotation
    }
    lines = [
        "\nfrom collections.abc import Sequence\n",
        "from typing import Any, Literal, Never, TypedDict, Unpack, overload\n",
        "from maya_brew.nodes._foundation.node_extensions import Node\n",
    ]
    if policy.node_imports:
        lines.append(
            f"from maya_brew.nodes.node_types import {', '.join(policy.node_imports)}\n"
        )
    lines.append(render_typed_dict(common_name, common))
    for name, fields in ((create_name, create_fields), (mode_name, mode_fields)):
        lines.append(
            render_typed_dict(
                name,
                {
                    flag: annotation
                    for flag, annotation in fields.items()
                    if flag not in common
                },
                common_name,
            )
        )
    lines.append(
        render_overload(
            command,
            policy.argument_type,
            create_name,
            [f"{flag}: Never = ..." for flag in policy.presence_flags],
            policy.creation_return_type,
        )
    )
    if policy.presence_return_type != "Any":
        for required in policy.presence_flags:
            lines.append(
                render_overload(
                    command,
                    policy.argument_type,
                    mode_name,
                    [
                        f"{flag}: {flags[flag]}"
                        + ("" if flag == required else " = ...")
                        for flag in policy.presence_flags
                    ],
                    policy.presence_return_type,
                )
            )
    lines.append(
        render_overload(
            command,
            policy.argument_type,
            mode_name,
            [f"{flag}: {flags[flag]} = ..." for flag in policy.presence_flags],
            "Any",
        )
    )
    return "".join(lines)
