# maya-brew

> **Status: Pre-Alpha** – Interfaces are experimental and may change without notice. Pin exact versions if using in
> automation.

What you need after a long day of wrestling with Maya Python.

[![Super-Linter](https://github.com/mortenbohne/maya-brew/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)

---

## Overview

`maya-brew` aims to provide safer, more structured interaction patterns when scripting or tooling inside Autodesk Maya.

Goals:

- Reduce foot‑guns when using Python inside Maya
- Offer utilities that behave well with Maya’s quirks

## Background

`maya-brew` draws inspiration from some of the ergonomic goals that motivated
[PyMEL](https://github.com/LumaPictures/pymel): making Maya’s Python interface feel more “Pythonic,” safer, and more
discoverable. PyMEL historically provided rich object wrappers around nodes, attributes, and other scene elements;
for many workflows this improved readability and reduced boilerplate.

However, over time several practical factors led to the decision to start a lightweight alternative instead of
extending PyMEL itself:

- Scope & Complexity: PyMEL’s dynamic wrapping and layered abstractions can introduce startup overhead, indirection, and
  occasional debugging friction.
- Historical Churn: A long evolution, multiple contributors, and some legacy design choices make selective modernization
  non‑trivial.
- Maintenance & Momentum: While still usable, PyMEL no longer appears to have the same pace of active development or
  broad community push it once did.
- Adoption Fit: Many pipelines only need a thin set of safety/ergonomic helpers—not a full object layer over
  `maya.cmds`.

### Acknowledgment

PyMEL significantly influenced how many technical artists approach Maya scripting, and this project stands on that
conceptual foundation. `maya-brew` simply narrows the focus: take the useful ergonomic ideas, shed the heavy wrapping,
and keep to the canonical APIs.

## Native node wrappers

User-facing exceptions are defined in `maya_brew.exceptions`. Catch specific
failures such as `NoMatchingNodes`, broader categories such as
`NodeCastingException`, or `MayaBrewException` for all library-defined errors.

Python node classes follow Maya's node-type inheritance, including intermediate
ancestors. `cast` selects the exact native class for an existing node;
direct constructors remain explicit.

```python
from maya_brew.nodes.casting import cast
from maya_brew.nodes.node_types import Transform

node = cast("my_transform")
assert isinstance(node, Transform)

transform = cast("my_transform", Transform)  # Typed and checked as Transform

```

### Command wrappers

`maya_brew.cmds` provides typed wrappers around selected `maya.cmds` commands.
Wrapper docstrings describe differences from Maya's behavior. Use `maya.cmds`
directly for commands that are not yet wrapped.

Currently wrapped commands:

- `connectJoint`
- `circle`
- `cone`
- `cylinder`
- `createNode`
- `ikHandle`
- `ikHandleDisplayScale`
- `ikSolver`
- `ikSystemInfo`
- `insertJoint`
- `joint`
- `jointDisplayScale`
- `ls`
- `mirrorJoint`
- `nurbsCube`
- `nurbsPlane`
- `nurbsSquare`
- `polyCone`
- `polyCube`
- `polyCylinder`
- `polyHelix`
- `polyPipe`
- `polyPlane`
- `polyPlatonicSolid`
- `polyPrimitive`
- `polyPrism`
- `polyPyramid`
- `polySphere`
- `polyTorus`
- `removeJoint`
- `sphere`
- `torus`

Regenerate wrappers and stubs with:

```bash
mayapy -m tools.generate
```

This command inspects the current Maya runtime, regenerates versioned node
hierarchy snapshots, and regenerates command wrapper runtime/stub files from
Maya help + tool metadata.

Generation internals and design notes live in docstrings under `tools/`.

### Generated hierarchies

Offline generation infrastructure lives in `tools/node_hierarchy`, outside the
installed runtime package. Its versioned outputs live exclusively in
`src/maya_brew/nodes/_generated/maya_<version>`:

| Artifact       | Purpose                                                     |
| -------------- | ----------------------------------------------------------- |
| `classes.py`   | Explicit, importable native classes                         |
| `constants.py` | `TYPE_CLASSES` mapping from Maya names to generated classes |

The runtime selects generated classes by Maya's major version, with runtime
fallback for missing releases or types.
