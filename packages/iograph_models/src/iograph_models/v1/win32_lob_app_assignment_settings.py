from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Win32LobAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.win32LobAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppAssignmentSettings")
	autoUpdateSettings: Optional[Win32LobAppAutoUpdateSettings] = Field(alias="autoUpdateSettings", default=None,)
	deliveryOptimizationPriority: Optional[Win32LobAppDeliveryOptimizationPriority | str] = Field(alias="deliveryOptimizationPriority", default=None,)
	installTimeSettings: Optional[MobileAppInstallTimeSettings] = Field(alias="installTimeSettings", default=None,)
	notifications: Optional[Win32LobAppNotification | str] = Field(alias="notifications", default=None,)
	restartSettings: Optional[Win32LobAppRestartSettings] = Field(alias="restartSettings", default=None,)

from .win32_lob_app_auto_update_settings import Win32LobAppAutoUpdateSettings
from .win32_lob_app_delivery_optimization_priority import Win32LobAppDeliveryOptimizationPriority
from .mobile_app_install_time_settings import MobileAppInstallTimeSettings
from .win32_lob_app_notification import Win32LobAppNotification
from .win32_lob_app_restart_settings import Win32LobAppRestartSettings
