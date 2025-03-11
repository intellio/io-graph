from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WinGetAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	installTimeSettings: Optional[WinGetAppInstallTimeSettings] = Field(alias="installTimeSettings",default=None,)
	notifications: Optional[WinGetAppNotification | str] = Field(alias="notifications",default=None,)
	restartSettings: Optional[WinGetAppRestartSettings] = Field(alias="restartSettings",default=None,)

from .win_get_app_install_time_settings import WinGetAppInstallTimeSettings
from .win_get_app_notification import WinGetAppNotification
from .win_get_app_restart_settings import WinGetAppRestartSettings

