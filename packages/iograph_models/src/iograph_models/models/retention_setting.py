from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RetentionSetting(BaseModel):
	interval: Optional[str] = Field(default=None,alias="interval",)
	period: Optional[str] = Field(default=None,alias="period",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


