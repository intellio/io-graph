from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosNotificationSettings(BaseModel):
	alertType: Optional[IosNotificationAlertType | str] = Field(alias="alertType", default=None,)
	appName: Optional[str] = Field(alias="appName", default=None,)
	badgesEnabled: Optional[bool] = Field(alias="badgesEnabled", default=None,)
	bundleID: Optional[str] = Field(alias="bundleID", default=None,)
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	previewVisibility: Optional[IosNotificationPreviewVisibility | str] = Field(alias="previewVisibility", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	showInNotificationCenter: Optional[bool] = Field(alias="showInNotificationCenter", default=None,)
	showOnLockScreen: Optional[bool] = Field(alias="showOnLockScreen", default=None,)
	soundsEnabled: Optional[bool] = Field(alias="soundsEnabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .ios_notification_alert_type import IosNotificationAlertType
from .ios_notification_preview_visibility import IosNotificationPreviewVisibility
