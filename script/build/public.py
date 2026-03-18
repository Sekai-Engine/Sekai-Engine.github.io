import os
import shutil
import re
import build.private as private

def page_build(ROOT, OUT, status):
    private.path_clear(OUT)
    private.static_copy(ROOT, OUT, "static")
    private.set_template(ROOT, OUT, "pages", "templates", "components", r"${pages.page_name}", status)
