import json

from aiohttp import web

routes = web.RouteTableDef()

class ApiCog:
  def __init__(self,app):
    self.app = app
    app.add_routes(routes)

    with open("src/data.json") as f:
      data = json.loads(f.read())
    
  def _getTrackedProjectsData(self):
    with open("src/data.json") as f:
      data = json.loads(f.read())
    

def setup(app):
  app.add_cog(ApiCog(app))
