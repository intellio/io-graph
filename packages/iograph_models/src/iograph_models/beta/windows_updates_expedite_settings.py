from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsUpdatesExpediteSettings(BaseModel):
	isExpedited: Optional[bool] = Field(alias="isExpedited", default=None,)
	isReadinessTest: Optional[bool] = Field(alias="isReadinessTest", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

