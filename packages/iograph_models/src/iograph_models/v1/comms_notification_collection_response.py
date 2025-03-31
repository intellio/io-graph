from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CommsNotificationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CommsNotification]] = Field(alias="value", default=None,)

from .comms_notification import CommsNotification
