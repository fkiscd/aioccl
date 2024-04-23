import asyncio
from aiohttp import web

async def handler(request):
  """AIOHTTP Handler for POST requests."""
  data = await request.post()
  payload = data.get("payload")
  return web.Response()

async def run():
  """Run the API server."""
  server = web.Server(handler)
  runner = server.ServerRunner()
  await runner.setup()
  site = web.TCPSite(runner, 'localhost', 8080)
  await site.start()
  
