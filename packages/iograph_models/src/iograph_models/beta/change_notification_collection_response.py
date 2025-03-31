from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChangeNotificationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ChangeNotification]] = Field(alias="value", default=None,)

from .change_notification import ChangeNotification
