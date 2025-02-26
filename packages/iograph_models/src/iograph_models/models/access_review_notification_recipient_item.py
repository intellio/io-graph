from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewNotificationRecipientItem(BaseModel):
	notificationRecipientScope: Optional[AccessReviewNotificationRecipientScope] = Field(default=None,alias="notificationRecipientScope",)
	notificationTemplateType: Optional[str] = Field(default=None,alias="notificationTemplateType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_review_notification_recipient_scope import AccessReviewNotificationRecipientScope

