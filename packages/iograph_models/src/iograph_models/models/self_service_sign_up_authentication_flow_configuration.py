from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SelfServiceSignUpAuthenticationFlowConfiguration(BaseModel):
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


