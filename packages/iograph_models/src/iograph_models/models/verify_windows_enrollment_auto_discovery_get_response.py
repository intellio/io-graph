from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Verify_windows_enrollment_auto_discoveryGetResponse(BaseModel):
	value: Optional[bool] = Field(default=None,alias="value",)


