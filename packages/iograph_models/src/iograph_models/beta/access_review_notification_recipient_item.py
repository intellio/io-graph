from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewNotificationRecipientItem(BaseModel):
	notificationRecipientScope: SerializeAsAny[Optional[AccessReviewNotificationRecipientScope]] = Field(alias="notificationRecipientScope",default=None,)
	notificationTemplateType: Optional[str] = Field(alias="notificationTemplateType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_review_notification_recipient_scope import AccessReviewNotificationRecipientScope

