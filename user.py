#!/usr/bin/env python
# -*- coding: utf-8 -*-

astr = "UPPER"

def init():
    print("init")

def handler(event, context):
    print (event)
    return "data %s=%s" % (astr, event.get("body").upper())
    
