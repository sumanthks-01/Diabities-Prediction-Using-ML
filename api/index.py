from app import app

# This is the entry point for Vercel
def handler(request):
    return app(request.environ, lambda status, headers: None)