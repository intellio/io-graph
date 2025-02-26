from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosNotificationSettings(BaseModel):
	alertType: Optional[IosNotificationAlertType] = Field(default=None,alias="alertType",)
	appName: Optional[str] = Field(default=None,alias="appName",)
	badgesEnabled: Optional[bool] = Field(default=None,alias="badgesEnabled",)
	bundleID: Optional[str] = Field(default=None,alias="bundleID",)
	enabled: Optional[bool] = Field(default=None,alias="enabled",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	showInNotificationCenter: Optional[bool] = Field(default=None,alias="showInNotificationCenter",)
	showOnLockScreen: Optional[bool] = Field(default=None,alias="showOnLockScreen",)
	soundsEnabled: Optional[bool] = Field(default=None,alias="soundsEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .ios_notification_alert_type import IosNotificationAlertType

