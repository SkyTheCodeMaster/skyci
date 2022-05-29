import json

from utils.multi_file_aiohttp import MultiFileRouteDef as RTD

routes = RTD()

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
