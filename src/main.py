import importlib.util
from typing import Optional

import aiohttp
from aiohttp import web
import aiohttp_jinja2
import jinja2

from utils.multi_file_aiohttp import MultiFileApplication

app = MultiFileApplication()

app.load_extension("cogs.frontend")
app.load_extension("cogs.error")

web.run_app(app,port=36750)