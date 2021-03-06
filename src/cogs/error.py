from aiohttp import web
import aiohttp_jinja2

async def handle404(request):
  return aiohttp_jinja2.render_template("errors/404.html",request,{},status=404)

async def handle500(request):
  return aiohttp_jinja2.render_template("errors/500.html",request,{},status=500)

def create_error_middleware(overrides):
  @web.middleware
  async def error_middleware(request, handler):
    try:
      print(handler.__code__.co_varnames)
      return await handler(handler.__self__,request)
    except web.HTTPException as ex:
      override = overrides.get(ex.status)
      if override:
        resp = await override(request)
        resp.set_status(ex.status)
        return resp
      raise
    except Exception:
      request.protocol.logger.exception("Error handling request")
      return await overrides[500](request)
  return error_middleware

def setup(app):
  error_middleware = create_error_middleware({
      404: handle404,
      500: handle500,
  })
  app.middlewares.append(error_middleware)
