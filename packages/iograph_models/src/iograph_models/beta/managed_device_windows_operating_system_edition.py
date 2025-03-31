from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceWindowsOperatingSystemEdition(BaseModel):
	editionType: Optional[ManagedDeviceWindowsOperatingSystemEditionType | str] = Field(alias="editionType", default=None,)
	supportEndDate: Optional[str] = Field(alias="supportEndDate", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .managed_device_windows_operating_system_edition_type import ManagedDeviceWindowsOperatingSystemEditionType
