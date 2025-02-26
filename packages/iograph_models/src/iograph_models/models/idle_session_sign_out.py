from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdleSessionSignOut(BaseModel):
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	signOutAfterInSeconds: Optional[int] = Field(default=None,alias="signOutAfterInSeconds",)
	warnAfterInSeconds: Optional[int] = Field(default=None,alias="warnAfterInSeconds",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


