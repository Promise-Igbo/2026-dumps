import azure.functions as func
from fastapi_app import app as fastapi_app
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html

function_app = func.FunctionApp()

# Create ASGI middleware to connect Azure Function -> FastAPI
asgi_middleware = func.AsgiMiddleware(fastapi_app)

@function_app.route(route="{*route}", auth_level=func.AuthLevel.ANONYMOUS)
async def fastapi_handler(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    """Proxy all HTTP traffic to FastAPI."""
    return await asgi_middleware.handle_async(req, context)


# Optional: expose OpenAPI JSON for Swagger UI
@fastapi_app.get("/api/openapi.json", include_in_schema=False)
async def openapi_json():
    return fastapi_app.openapi()


@fastapi_app.get("/api/docs", include_in_schema=False)
async def custom_swagger_ui_html() -> HTMLResponse:
    """Custom Swagger UI endpoint that works with Azure Functions."""
    return get_swagger_ui_html(
        openapi_url="",  # empty because spec is passed directly
        title=f"{fastapi_app.title} - Swagger UI",
        swagger_ui_parameters={"spec": fastapi_app.openapi()},
    )