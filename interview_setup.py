#!/usr/bin/env python

from virl2_tools import interview


candidate = interview.Candidate("Jon", "Smith")
environment = interview.Environment(candidate)
environment.create()
