"""
The group module contains all income/expense group related stuff.
"""

from typing import Union


class Group:
    """
    A Group groups one or more income or expense entries or further sub-groups.
    The group implements the needed IPython repl formatting methods for
    outputting HTML, Mardkown and LaTeX. This is the intended way of displaying
    the data for the report. Use Jupyter's Markdown blocks to further structure
    and formate the budget and adding remarks for entries.
    """
