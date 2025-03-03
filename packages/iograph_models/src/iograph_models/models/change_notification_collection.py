from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChangeNotificationCollection(BaseModel):
	validationTokens: Optional[list[str]] = Field(default=None,alias="validationTokens",)
	value: Optional[list[ChangeNotification]] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .change_notification import ChangeNotification

