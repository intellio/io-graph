from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class WindowsManagementApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsManagementApp"] = Field(alias="@odata.type", default="#microsoft.graph.windowsManagementApp")
	availableVersion: Optional[str] = Field(alias="availableVersion", default=None,)
	managedInstaller: Optional[ManagedInstallerStatus | str] = Field(alias="managedInstaller", default=None,)
	managedInstallerConfiguredDateTime: Optional[str] = Field(alias="managedInstallerConfiguredDateTime", default=None,)
	healthStates: Optional[list[WindowsManagementAppHealthState]] = Field(alias="healthStates", default=None,)

from .managed_installer_status import ManagedInstallerStatus
from .windows_management_app_health_state import WindowsManagementAppHealthState
