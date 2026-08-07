"""The console has to survive the terminal it is given."""

from django_shadcn.console import _use_utf8


class Refuses:
    """A stream that advertises reconfigure and then rejects it."""

    def reconfigure(self, **kwargs):
        raise OSError('stream is detached')


class Wrong:
    def reconfigure(self, **kwargs):
        raise ValueError('unsupported encoding')


class Plain:
    """A stream from before reconfigure existed."""


def test_a_stream_that_cannot_be_reconfigured_is_left_alone():
    """A redirected or detached stdout must not take the CLI down with it."""
    _use_utf8(Refuses())
    _use_utf8(Wrong())
    _use_utf8(Plain())
