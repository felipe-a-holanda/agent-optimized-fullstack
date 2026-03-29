from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://app:app@localhost:54325/app"
    app_name: str = "{{ project_slug }}"
    debug: bool = True

    # Auth
    secret_key: str = "CHANGE-ME-IN-PRODUCTION"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    algorithm: str = "HS256"

    # Admin
    admin_email: str = "admin@example.com"
    admin_password: str = "admin"

    # Root .env is the single source of truth; .env here is for local overrides
    model_config = SettingsConfigDict(env_file=["../../.env", ".env"], extra="ignore")


settings = Settings()
