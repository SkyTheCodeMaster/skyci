from aiohttp import web
import aiohttp_jinja2

async def handle404(request):
  return aiohttp_jinja2.render_template("404.html",request,{},status=404)

def create_error_middleware(overrides):
  @web.middleware
  async def error_middleware(request, handler):
    try:
      return await handler(request)
    except web.HTTPException as ex:
      override = overrides.get(ex.status)
      if override:
        return await override(request)
        raise
    except Exception:
      request.protocol.logger.exception("Error handling request")
      return await overrides[500](request)
  return error_middleware

def setup(app):
  error_middleware = create_error_middleware({
      404: handle404
  })
  app.middlewares.append(error_middleware)
