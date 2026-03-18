#!/bin/python3

import os
import build.public as build
import shell.public as shell
import server.public as server

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
OUT = os.path.join(ROOT, "_site")
VERSION = "v0.0.1"

result_shell = shell.options(VERSION)
build.page_build(ROOT, OUT, result_shell["status"][0])

if result_shell["force"]:
    server.try_kill_port(result_shell["port"][0])
    
if result_shell["status"][0] == "debug":
    server.sekai_server(OUT, result_shell["port"][0])

