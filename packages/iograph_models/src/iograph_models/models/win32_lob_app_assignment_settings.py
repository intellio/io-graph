from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	autoUpdateSettings: Optional[Win32LobAppAutoUpdateSettings] = Field(default=None,alias="autoUpdateSettings",)
	deliveryOptimizationPriority: Optional[Win32LobAppDeliveryOptimizationPriority] = Field(default=None,alias="deliveryOptimizationPriority",)
	installTimeSettings: Optional[MobileAppInstallTimeSettings] = Field(default=None,alias="installTimeSettings",)
	notifications: Optional[Win32LobAppNotification] = Field(default=None,alias="notifications",)
	restartSettings: Optional[Win32LobAppRestartSettings] = Field(default=None,alias="restartSettings",)

from .win32_lob_app_auto_update_settings import Win32LobAppAutoUpdateSettings
from .win32_lob_app_delivery_optimization_priority import Win32LobAppDeliveryOptimizationPriority
from .mobile_app_install_time_settings import MobileAppInstallTimeSettings
from .win32_lob_app_notification import Win32LobAppNotification
from .win32_lob_app_restart_settings import Win32LobAppRestartSettings

