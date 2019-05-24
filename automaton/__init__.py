"""Automaton"""
# !/usr/bin/env/python
import sys
import logging
from os import environ
from .automaton import Automaton

try:
    if "AUTOMATON_LOGLEVEL" in environ:
        logging.basicConfig(
            stream=sys.stdout,
            level=environ.get("AUTOMATON_LOGLEVEL"),
            format="%(asctime)s %(name)s %(levelname)s" + " %(message)s ",
        )
    else:
        logging.basicConfig(
            stream=sys.stdout,
            level="INFO",
            format="%(asctime)s %(name)s %(levelname)s" + " %(message)s ",
        )
    logger = logging.getLogger(__name__)
except (KeyError, ValueError, AttributeError, Exception) as error:
    raise
