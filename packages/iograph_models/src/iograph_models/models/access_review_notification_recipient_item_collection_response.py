from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewNotificationRecipientItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AccessReviewNotificationRecipientItem] = Field(alias="value",)

from .access_review_notification_recipient_item import AccessReviewNotificationRecipientItem

