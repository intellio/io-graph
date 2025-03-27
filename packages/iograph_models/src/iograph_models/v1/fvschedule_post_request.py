from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FvschedulePostRequest(BaseModel):
	principal: Optional[str] = Field(alias="principal", default=None,)
	schedule: Optional[str] = Field(alias="schedule", default=None,)


