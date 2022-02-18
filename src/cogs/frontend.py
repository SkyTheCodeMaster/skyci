from aiohttp import web

routes = web.RouteTableDef()

class FrontendCog:
  def __init__(self,app):
    self.app = app
    app.add_routes(routes)

  @routes.get("/")
  async def hello(request):
    return web.Response(text="Hello world lmao")

def setup(app):
  app.add_cog(FrontendCog(app))