dancemachine
============

## Control iTunes on OS X using Python

    $ python
    >>> from dancemachine import transport
    >>> transport.play()
    >>> transport.next()
    <dancemachine.Track object at 0x106e834d0>
    >>> print transport.now_playing()
    "Break" by Fugazi from the album "End Hits"
    >>> print transport.next(fade=True)
    "Speed King" by Deep Purple from the album "In Rock"
    >>> transport.fade_out()


