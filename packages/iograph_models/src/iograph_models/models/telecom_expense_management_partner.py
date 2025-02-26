from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TelecomExpenseManagementPartner(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appAuthorized: Optional[bool] = Field(default=None,alias="appAuthorized",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	enabled: Optional[bool] = Field(default=None,alias="enabled",)
	lastConnectionDateTime: Optional[datetime] = Field(default=None,alias="lastConnectionDateTime",)
	url: Optional[str] = Field(default=None,alias="url",)


