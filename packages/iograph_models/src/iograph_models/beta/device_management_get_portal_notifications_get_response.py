from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Device_management_get_portal_notificationsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceManagementPortalNotification]] = Field(alias="value", default=None,)

from .device_management_portal_notification import DeviceManagementPortalNotification
