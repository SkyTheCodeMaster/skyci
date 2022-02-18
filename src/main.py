import importlib.util
from typing import Optional

import aiohttp
from aiohttp import web
import aiohttp_jinja2
import jinja2

class MultiFileApplication(web.Application):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.cogs = {}
    aiohttp_jinja2.setup(self,loader=jinja2.FileSystemLoader("src/templates"))

  def _get_module(self,name:str,*,package=None):
    n = importlib.util.resolve_name(name,package)
    spec = importlib.util.find_spec(n)
    lib = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lib)
    return lib

  def load_extension(self,name:str,*,package=None):
    try:
      lib = self._get_module(name,package=package)
      lib.setup(self)
    except Exception as e:
      raise

  def add_cog(self,cog):
    self.cogs[cog.__name__] = cog

app = MultiFileApplication()

app.load_extension("cogs.frontend")
app.load_extension("cogs.error")

web.run_app(app,port=36750)