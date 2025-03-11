from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrainingReminderNotification(BaseModel):
	defaultLanguage: Optional[str] = Field(alias="defaultLanguage",default=None,)
	endUserNotification: Optional[EndUserNotification] = Field(alias="endUserNotification",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deliveryFrequency: Optional[NotificationDeliveryFrequency | str] = Field(alias="deliveryFrequency",default=None,)

from .end_user_notification import EndUserNotification
from .notification_delivery_frequency import NotificationDeliveryFrequency

