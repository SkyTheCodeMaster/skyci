import importlib.util
from typing import Any

import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp.web_routedef import _HandlerType,RouteDef,_Deco

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
    self.cogs[cog.__class__.__name__] = cog

class MultiFileRouteDef(web.RouteTableDef):
  # This patches the "self" parameter in classes, by simply dropping it.
  def route(self, method: str, path: str, **kwargs: Any) -> _Deco:
    def inner(handler: _HandlerType) -> _HandlerType:
      self._items.append(RouteDef(method, path, handler, kwargs))
      async def _inner(request):
        return await handler(request)
      return _inner
    return inner