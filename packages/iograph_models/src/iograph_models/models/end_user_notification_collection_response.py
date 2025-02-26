from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EndUserNotificationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[EndUserNotification] = Field(alias="value",)

from .end_user_notification import EndUserNotification

