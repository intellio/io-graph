from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsManagementApp(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	availableVersion: Optional[str] = Field(alias="availableVersion", default=None,)
	managedInstaller: Optional[ManagedInstallerStatus | str] = Field(alias="managedInstaller", default=None,)
	managedInstallerConfiguredDateTime: Optional[str] = Field(alias="managedInstallerConfiguredDateTime", default=None,)
	healthStates: Optional[list[WindowsManagementAppHealthState]] = Field(alias="healthStates", default=None,)

from .managed_installer_status import ManagedInstallerStatus
from .windows_management_app_health_state import WindowsManagementAppHealthState

