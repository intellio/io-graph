from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrainingReminderNotification(BaseModel):
	defaultLanguage: Optional[str] = Field(default=None,alias="defaultLanguage",)
	endUserNotification: Optional[EndUserNotification] = Field(default=None,alias="endUserNotification",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deliveryFrequency: Optional[NotificationDeliveryFrequency] = Field(default=None,alias="deliveryFrequency",)

from .end_user_notification import EndUserNotification
from .notification_delivery_frequency import NotificationDeliveryFrequency

