from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TodoSettings(BaseModel):
	isExternalJoinEnabled: Optional[bool] = Field(alias="isExternalJoinEnabled", default=None,)
	isExternalShareEnabled: Optional[bool] = Field(alias="isExternalShareEnabled", default=None,)
	isPushNotificationEnabled: Optional[bool] = Field(alias="isPushNotificationEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

