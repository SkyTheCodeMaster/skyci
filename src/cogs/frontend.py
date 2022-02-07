from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def hello(request):
  return web.Response(text="Hello world lmao")

def setup(app):
  app.add_routes(routes)