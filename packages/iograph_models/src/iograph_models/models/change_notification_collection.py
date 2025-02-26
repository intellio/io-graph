from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChangeNotificationCollection(BaseModel):
	validationTokens: list[Optional[str]] = Field(alias="validationTokens",)
	value: list[ChangeNotification] = Field(alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .change_notification import ChangeNotification

