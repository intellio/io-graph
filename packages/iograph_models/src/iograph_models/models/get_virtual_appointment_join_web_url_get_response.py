from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_virtual_appointment_join_web_urlGetResponse(BaseModel):
	value: Optional[str] = Field(default=None,alias="value",)


