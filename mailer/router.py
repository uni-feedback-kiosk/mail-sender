from fastapi import status, Depends
from fastapi.routing import APIRouter
from fastapi.responses import Response
from email.message import EmailMessage
import aiosmtplib

from mailer import settings
from mailer.dependencies import ensure_bearer_token
from mailer.schemas import EmailData

mail_router = APIRouter(
    tags=["Mail"],
    dependencies=[
        Depends(ensure_bearer_token),
    ],
)


@mail_router.post(
    "/send", status_code=status.HTTP_204_NO_CONTENT, response_class=Response
)
async def send_mail(email: EmailData):
    message = EmailMessage()
    message["From"] = f'"{settings.sender_name}" <{settings.smtp_username}>'
    message["To"] = settings.mail_recipient
    message["Subject"] = email.subject
    message.set_content(email.body, subtype="html")

    await aiosmtplib.send(
        message,
        sender=message["From"],
        hostname=settings.smtp_host,
        port=settings.smtp_port,
        username=settings.smtp_username,
        password=settings.smtp_password,
        start_tls=True,
    )
