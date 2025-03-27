from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementNotificationChannel(BaseModel):
	notificationChannelType: Optional[DeviceManagementNotificationChannelType | str] = Field(alias="notificationChannelType", default=None,)
	notificationReceivers: Optional[list[DeviceManagementNotificationReceiver]] = Field(alias="notificationReceivers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_notification_channel_type import DeviceManagementNotificationChannelType
from .device_management_notification_receiver import DeviceManagementNotificationReceiver

