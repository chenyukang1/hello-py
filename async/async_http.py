from aiohttp import web


async def index(request):
    text = "<h1>Index Page</h1>"
    return web.Response(text=text, content_type="text/html")


async def hello(request):
    name = request.match_info.get("name", "World")
    text = f"<h1>Hello, {name}</h1>"
    return web.Response(text=text, content_type="text/html")


app = web.Application()
app.add_routes([web.get("/", index), web.get("/{name}", hello)])
web.run_app(app=app)
