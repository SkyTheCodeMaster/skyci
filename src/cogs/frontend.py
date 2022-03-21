from aiohttp import web
import aiohttp_jinja2

routes = web.RouteTableDef()

class FrontendCog:
  def __init__(self,app):
    self.app = app
    app.add_routes(routes)

  @routes.get("/")
  async def get_root(self,request):
    projects = self.app.projects
    return aiohttp_jinja2.render_template("root.html",request,{},status=200)


def setup(app):
  routes.static("/assets","src/assets")
  app.add_cog(FrontendCog(app))