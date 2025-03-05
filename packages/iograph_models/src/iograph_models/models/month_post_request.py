from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MonthPostRequest(BaseModel):
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)


