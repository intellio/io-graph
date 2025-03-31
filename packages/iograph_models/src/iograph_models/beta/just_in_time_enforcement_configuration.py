from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class JustInTimeEnforcementConfiguration(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

