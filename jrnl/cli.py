#!/usr/bin/env python
# Copyright (C) 2012-2021 jrnl contributors
# License: https://www.gnu.org/licenses/gpl-3.0.html

import logging
import sys

from .jrnl import run
from .args import parse_args
from .exception import ConfigDirectoryPathIsFileException


def configure_logger(debug=False):
    if not debug:
        logging.disable()
        return

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)-8s %(name)-12s %(message)s",
    )
    logging.getLogger("parsedatetime").setLevel(logging.INFO)
    logging.getLogger("keyring.backend").setLevel(logging.ERROR)


def cli(manual_args=None):
    try:
        if manual_args is None:
            manual_args = sys.argv[1:]

        args = parse_args(manual_args)
        configure_logger(args.debug)
        logging.debug("Parsed args: %s", args)

        return run(args)

    except ConfigDirectoryPathIsFileException as e:
        print(e, file=sys.stderr)
        return 1

    except KeyboardInterrupt:
        return 1
