from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_mobile_device_management_authorityPostResponse(BaseModel):
	value: Optional[int] = Field(default=None,alias="value",)


