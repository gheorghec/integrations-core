# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from .common import HERE


def mock_systemd_output(fname):
    with open(os.path.join(HERE, 'fixtures', fname)) as f:
        return f.read()
