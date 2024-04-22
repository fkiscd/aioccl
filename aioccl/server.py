import asyncio
from aiohttp import web

async def handle_post(request):
  """AIOHTTP Handler for POST requests."""
  data = await request.post()
  
  return web.Response()

server = web.Server()
app.router.add_post('/', handle_post)

async def start_server():
  """Start the API server."""
  runner = server.ServerRunner()
  await runner.setup()
  site = web.TCPSite(runner, 'localhost', 8080)
  await site.start()
  
