from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppInstallExperience(BaseModel):
	deviceRestartBehavior: Optional[Win32LobAppRestartBehavior | str] = Field(alias="deviceRestartBehavior", default=None,)
	runAsAccount: Optional[RunAsAccountType | str] = Field(alias="runAsAccount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .win32_lob_app_restart_behavior import Win32LobAppRestartBehavior
from .run_as_account_type import RunAsAccountType
