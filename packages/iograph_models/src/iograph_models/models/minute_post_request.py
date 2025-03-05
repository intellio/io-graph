from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MinutePostRequest(BaseModel):
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)


