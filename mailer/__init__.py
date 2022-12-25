from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .settings import settings
from .router import mail_router

app = FastAPI(
    title="kiosk-mail-sender", version="1.0", default_response_class=ORJSONResponse
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mail_router)
