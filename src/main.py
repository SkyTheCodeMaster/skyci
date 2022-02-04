import importlib.util
from typing import Optional

import aiohttp
from aiohttp import web

class MultiFileApplication(web.Application):
  def load_extension(self,name:str,*,package:Optional[str]=None):
    try:
      n = importlib.util.resolve_name(name,package)
      spec = importlib.util.find_spec(n)
      lib = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(lib)
      lib.setup(self)
    except Exception as e:
      raise

app = MultiFileApplication()

app.load_extension("cogs.frontend")

web.run_app(app,port=36750)