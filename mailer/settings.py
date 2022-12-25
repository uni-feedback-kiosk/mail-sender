from pydantic import BaseSettings


class Settings(BaseSettings):
    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    sender_name: str
    mail_recipient: str
    bearer_token: str

    class Config:
        env_file = ".env"  # Use .env file for local development
        env_prefix = "MAILER_"


settings = Settings()
