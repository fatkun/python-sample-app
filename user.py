#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("outside")

a = "test"

def init():
    print("init")

def handler(event, context):
    print (event)
    return "data =%s %s" % (a, event['data'])