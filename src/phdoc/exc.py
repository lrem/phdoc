# -*- coding: utf-8 -*-


class MarkdocError(Exception):
    """An error occurred whilst running the phdoc utility."""
    pass


class AbortError(MarkdocError):
    """An exception occurred which should cause Markdoc to abort."""
    pass

