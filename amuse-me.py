#!/usr/bin/env python
#-*- coding: utf-8 -*-

import curses
import time
import base64
import random

D = 'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg' + \
    'ICAgICAgICAgICAgICAgICBTICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg' + \
    'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApICAgICAg' + \
    'ICAgKCAgICAgICAgICkgICAgICAgICAgICAgICAgICAgICBDICAgICAgICAgICAp' + \
    'IChfKSAgICggICAoXykgICApICAgKF8pICggICAgICAgICAgICAgICBCICAgICAg' + \
    'ICAgICAgIChfKSAjICkgKF8pICkgIyAoIChfKSAoICMgKF8pICAgICAgICAgICAg' + \
    'ICAgICBIICAgICAgICAgIF8jLi0jKF8pLSMtKF8pIyhfKS0jLShfKSMtLiNfICAg' + \
    'ICAgICAgICAgICBJICAgICAgICAgICAuJyAjICAjICMgICMgICMgIyAjICAjICAj' + \
    'ICMgICMgYC4gICAgICAgICBIICAgICBFICAgICAgIDogICAjICAgICMgICMgICMg' + \
    'ICAjICAjICAjICAgICMgICA6ICAgICAgICAgICBSICAgICAgICAgIDouICAgICAg' + \
    'ICMgICAgICMgICAjICAgICAjICAgICAgIC46ICAgICAgICBBICAgICBJICAgICAg' + \
    'IHwgYC0uX18gICAgICAgICAgICAgICAgICAgICBfXy4tJyB8ICAgICAgICAgICBU' + \
    'ICAgICAgICAgIHwgICAgICBgYGBgYCIiIiIiIiIiIiIiYGBgYGAgICAgICB8ICAg' + \
    'ICAgICBQICAgICBEICAgICAgIHwgICAgICAgICAgICAgICAgICAgICAgICAgICAg' + \
    'ICAgICB8ICAgICAgICAgICBIICAgICAgICAgIDouICAgICAgICAgICAgICAgICAg' + \
    'ICAgICAgICAgICAgIC46ICAgICAgICBQICAgICBFICAgICAgIHwgYC0uX18gICAg' + \
    'ICAgICAgICAgICAgICAgICBfXy4tJyB8ICAgICAgICAgICBEICAgICAgICAgIHwg' + \
    'ICAgICBgYGBgYCIiIiIiIiIiIiIiYGBgYGAgICAgICB8ICAgICAgICBZICAgICBH' + \
    'ICAgIF8uLXwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8LS5fICAg' + \
    'ICAgICBBICAgICAuJyAgICcuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg' + \
    'IC4nICAgYC4gICAgICAgICBHICA6ICAgICAgYC0uX18gICAgICAgICAgICAgICAg' + \
    'ICAgICBfXy4tJyAgICAgIDogICAgICBZICAgICAgYC4gICAgICAgICBgYGBgYCIi' + \
    'IiIiIiIiIiIiYGBgYGAgICAgICAgICAuJyAgICAgICAgICBFICAgICBgLS4uXyAg' + \
    'ICAgICAgICAgICAgICAgICAgICAgICAgICAgXy4uLScgICAgICAgICAgICAgICAg' + \
    'ICAgICAgIGBgYGBgIiIiIi0tLS0tLS0tLS0tIiIiImBgYGBgICAgICAgICAgICAg' + \
    'ICAgICBSICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg' + \
    'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg' + \
    'ICAgICAgICAgICAgICAg'

D = base64.b64decode(D)
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
pad = curses.newpad(23, 58)
for y in range(0, 23):
    for x in range(0, 57):
        try: pad.addch(y, x, D[y * 57 + x])
        except curses.error: pass
pad.refresh(0, 0, 0, 0, 23, 57)
try:
    while True:
        for x, y in [(2, 23), (2, 33), (2, 43), (3, 20), (3, 28), (3, 38),
                     (3, 46), (4, 25), (4, 31), (4, 35), (4, 41)]:
            pad.addch(x, y, random.choice([')', '(']))
            pad.refresh(x, y, x, y, x, y)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

