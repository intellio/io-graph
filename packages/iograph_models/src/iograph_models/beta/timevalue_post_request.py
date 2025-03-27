from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TimevaluePostRequest(BaseModel):
	timeText: Optional[str] = Field(alias="timeText", default=None,)


