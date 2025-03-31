from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RetentionSetting(BaseModel):
	interval: Optional[str] = Field(alias="interval", default=None,)
	period: Optional[str] = Field(alias="period", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

