#!/bin/python3

import os
import build.public as build
import shell.public as shell

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
OUT = os.path.join(ROOT, "_site")
VERSION = "v0.0.1"

result_shell = shell.options(VERSION)
build.page_build(ROOT, OUT)

if result_shell["status"][0] == "debug":
    import server.public as server
    server.sekai_server(OUT, result_shell["port"][0])
