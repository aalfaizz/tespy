# -*- coding: utf-8
import logging

from tespy.tools.helpers import TESPyNetworkError

# %%


class network:
    r"""Throw errors for deprecated classes."""

    def __init__(self, *args, **kwargs):
        msg = (
            'Version 0.4.x introduced PEP 8 conform class names for all '
            'classes used in TESPy. Please refer to '
            'https://tespy.readthedocs.io/en/master/whats_new.html '
            'learn about the changes necessary to adapt your script to the '
            'latest API.'
        )
        logging.error(msg)
        raise TESPyNetworkError(msg)
