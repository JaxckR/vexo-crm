from dataclasses import dataclass
from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
SETTINGS_DIR = BASE_DIR.parent


@dataclass(frozen=True, slots=True)
class PostgresConfig:
    user: str
    password: str
    host: str
    port: int
    database: str

    @property
    def url(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass(frozen=True, slots=True)
class Config:
    database: PostgresConfig


def get_config() -> Config:
    return Config(
        database=PostgresConfig(
            user=getenv("POSTGRES_USER"),
            password=getenv("POSTGRES_PASSWORD"),
            host=getenv("POSTGRES_HOST"),
            port=int(getenv("POSTGRES_PORT")),
            database=getenv("POSTGRES_DATABASE"),
        )
    )
