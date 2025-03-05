from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppInstallExperience(BaseModel):
	deviceRestartBehavior: Optional[Win32LobAppRestartBehavior] = Field(default=None,alias="deviceRestartBehavior",)
	runAsAccount: Optional[RunAsAccountType] = Field(default=None,alias="runAsAccount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .win32_lob_app_restart_behavior import Win32LobAppRestartBehavior
from .run_as_account_type import RunAsAccountType

