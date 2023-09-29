#!/usr/bin/env python3

import subprocess

proc = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
