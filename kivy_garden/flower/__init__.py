"""
Demo flower
============

Defines the Kivy garden :class:`FlowerLabel` class which is the widget provided
by the demo flower.
"""

from kivy.uix.label import Label

__all__ = ('FlowerLabel', )

__version__ = '0.1.0.dev0'


class FlowerLabel(Label):

    def __init__(self, **kwargs):
        super(FlowerLabel, self).__init__(**kwargs, text='Demo flower')
