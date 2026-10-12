class MayaBrewException(Exception):
    """Base class for all MayaBrew exceptions."""

    pass


class MayaBrewAttributeError(MayaBrewException, AttributeError):
    """Raised when there is an attribute-related error in MayaBrew."""

    pass


class SceneException(MayaBrewException):
    """Base class for scene-related exceptions."""


class UnsavedChanges(SceneException, RuntimeError):
    """Raised when scene changes have not been saved."""


class NodeException(MayaBrewException):
    """Raised when a node operation fails."""


class AbstractNodeCreationError(NodeException):
    """Raised when attempting to create an abstract node class."""


class NodeTypeInheritanceError(MayaBrewException):
    """Raised when Maya's node-type inheritance cannot be resolved."""


class NodeCastingException(MayaBrewException):
    """Base class for node casting exceptions."""


class InvalidDagPath(NodeCastingException, RuntimeError, ValueError, TypeError):
    """Raised when an existing object is not a DAG node."""


class NonExistingDagPath(NodeCastingException, RuntimeError, ValueError, TypeError):
    """Raised when a DAG path does not exist."""


class MultipleMatchingNodes(NodeCastingException):
    """Raised when multiple nodes match a name."""


class NoMatchingNodes(NodeCastingException):
    """Raised when no nodes match a name."""
