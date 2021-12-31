#!/usr/bin/env python3

import json
import sys

matrix = json.load(sys.stdin)
for job in matrix["include"]:
    print(f"{job['color']}-{job['animal']}")
