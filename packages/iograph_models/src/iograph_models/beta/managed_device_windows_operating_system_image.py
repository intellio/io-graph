from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedDeviceWindowsOperatingSystemImage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	availableUpdates: Optional[list[ManagedDeviceWindowsOperatingSystemUpdate]] = Field(alias="availableUpdates",default=None,)
	supportedArchitectures: Optional[list[ManagedDeviceArchitecture | str]] = Field(alias="supportedArchitectures",default=None,)
	supportedEditions: Optional[list[ManagedDeviceWindowsOperatingSystemEdition]] = Field(alias="supportedEditions",default=None,)

from .managed_device_windows_operating_system_update import ManagedDeviceWindowsOperatingSystemUpdate
from .managed_device_architecture import ManagedDeviceArchitecture
from .managed_device_windows_operating_system_edition import ManagedDeviceWindowsOperatingSystemEdition

