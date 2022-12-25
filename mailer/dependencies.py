import secrets
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Security, HTTPException, status

from mailer import settings

security = HTTPBearer()


async def ensure_bearer_token(
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> None:
    success = secrets.compare_digest(
        credentials.credentials.encode("utf8"), settings.bearer_token.encode("utf8")
    )
    if success:
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect auth",
        headers={"WWW-Authenticate": "Bearer"},
    )
