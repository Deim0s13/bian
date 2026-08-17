class EngineError(Exception):
    """Base error for expected engine failures."""


class SourceFormatError(EngineError):
    """The source cannot be safely interpreted by an adapter."""


class ModelValidationError(EngineError):
    """The canonical model violates one or more invariants."""
