from dataclasses import dataclass
from datetime import datetime
from typing import TypeVar, Generic

IdType = TypeVar("IdType")


@dataclass
class IDEntity(Generic[IdType]):
    id: IdType


@dataclass
class TimeStampEntity:
    created_at: datetime
    updated_at: datetime | None
