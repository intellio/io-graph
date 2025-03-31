from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AccessReviewNotificationRecipientItem(BaseModel):
	notificationRecipientScope: Optional[Union[AccessReviewNotificationRecipientQueryScope]] = Field(alias="notificationRecipientScope", default=None,discriminator="odata_type", )
	notificationTemplateType: Optional[str] = Field(alias="notificationTemplateType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .access_review_notification_recipient_query_scope import AccessReviewNotificationRecipientQueryScope
