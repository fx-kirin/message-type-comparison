#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 fx-kirin <fx.kirin@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import logging
import os
import pickle
from pathlib import Path

import msgpack
import numpy as np
from benchmarker import Benchmarker

import cbor2
import kanilog
import msgpack_numpy as m
import orjson
import stdlogging

m.patch()


def default(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()


def main():
    logging.info("Comparing numpy")
    a = np.arange(100000.0)

    with Benchmarker(100000, width=50) as bench:

        @bench("message_pack")
        def _(bm):
            data = msgpack.packb(a)
            msgpack.unpackb(data)

        for i in range(5):

            @bench("pickle %s" % (i))
            def _(bm):
                data = pickle.dumps(a, protocol=i)
                pickle.loads(data)

    logging.info("Comparing PyList")
    a = list([float(v) for v in a])
    with Benchmarker(100000, width=50) as bench:

        @bench("cbor2.dump")
        def _(bm):
            data = cbor2.dumps(a)
            cbor2.loads(data)

        @bench("message_pack")
        def _(bm):
            data = msgpack.packb(a)
            msgpack.unpackb(data)

        @bench("orjson")
        def _(bm):
            data = orjson.dumps(a)
            orjson.loads(data)

        for i in range(5):

            @bench("pickle %s" % (i))
            def _(bm):
                data = pickle.dumps(a, protocol=i)
                pickle.loads(data)


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    kanilog.setup_logger(
        logfile="/tmp/%s.log" % (Path(__file__).name), level=logging.INFO
    )
    stdlogging.enable()
    main()
