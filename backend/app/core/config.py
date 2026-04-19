import os

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://banker:password@postgres:5432/banker"
    )

    CURRENT_YEAR = 1405

settings = Settings()
