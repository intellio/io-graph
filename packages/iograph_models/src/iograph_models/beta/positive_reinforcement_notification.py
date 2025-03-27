from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class PositiveReinforcementNotification(BaseModel):
	defaultLanguage: Optional[str] = Field(alias="defaultLanguage", default=None,)
	endUserNotification: Optional[EndUserNotification] = Field(alias="endUserNotification", default=None,)
	odata_type: Literal["#microsoft.graph.positiveReinforcementNotification"] = Field(alias="@odata.type", default="#microsoft.graph.positiveReinforcementNotification")
	deliveryPreference: Optional[NotificationDeliveryPreference | str] = Field(alias="deliveryPreference", default=None,)

from .end_user_notification import EndUserNotification
from .notification_delivery_preference import NotificationDeliveryPreference

