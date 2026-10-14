from enum import IntEnum


class NodeState(IntEnum):
    NORMAL = 0
    HAS_NO_EFFECT = 1
    BLOCKING = 2
    # Maya uses waiting states temporarily during interaction, then restores 0-2.
    WAITING_NORMAL = 3
    WAITING_HAS_NO_EFFECT = 4
    WAITING_BLOCKING = 5
