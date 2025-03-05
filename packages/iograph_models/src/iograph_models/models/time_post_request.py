from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TimePostRequest(BaseModel):
	hour: Optional[str] = Field(default=None,alias="hour",)
	minute: Optional[str] = Field(default=None,alias="minute",)
	second: Optional[str] = Field(default=None,alias="second",)


