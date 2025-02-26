from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityRetentionDurationInDays(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	days: Optional[int] = Field(default=None,alias="days",)


