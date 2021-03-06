#! /usr/bin/python

# -*- Mode: Python -*-
# -*- coding: UTF-8 -*-
# Copyright (C) 2009 by Artur Ventura
#
# File: app.py
# Time-stamp: Sun Aug  9 16:30:18 2009
#
# Author: Artur Ventura
#


import web
import commands

urls = (
    '/(.*)', 'index',
    
)
app = web.application(urls, globals())

class index:
    def GET(self,filename):
        if filename.endswith("favicon.ico"):
            web.webapi.notfound()
            return ""
        if filename == "jvm.js":
            web.header('Content-Type', 'text/javascript')
            return commands.getstatusoutput("cat ../src/*.js | cpp -DDEBUG -DDEBUG_INTRP -I../src/ -P -undef -CC -Wundef -std=c99 -nostdinc -Wtrigraphs -fdollars-in-identifiers")[1]
        if "testRuntime" in filename:
            alphex = filename[filename.rfind("/") + 1:];
            return file("../runtime/" + alphex.replace(".","/") + ".class").read();
        if filename == "":
            return file("index.html").read()
        try:
            return file(filename).read()
        except:
            web.webapi.notfound()
            return ""
                
        

if __name__ == "__main__":
    app.run()
