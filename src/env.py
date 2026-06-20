"""Environment configuration loader."""

from __future__ import annotations

import os

from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    """Load environment variables from .env file.

    Returns:
        Dictionary of environment variable values.
    """
    load_dotenv()
    return {
        "FARSHID_API_KEY": os.environ.get("FARSHID_API_KEY"),
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
    }


if __name__ == "__main__":
    config = load_config()
    print("Config loaded successfully")
