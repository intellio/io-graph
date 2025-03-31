from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsPackageInformation(BaseModel):
	applicableArchitecture: Optional[WindowsArchitecture | str] = Field(alias="applicableArchitecture", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	identityName: Optional[str] = Field(alias="identityName", default=None,)
	identityPublisher: Optional[str] = Field(alias="identityPublisher", default=None,)
	identityResourceIdentifier: Optional[str] = Field(alias="identityResourceIdentifier", default=None,)
	identityVersion: Optional[str] = Field(alias="identityVersion", default=None,)
	minimumSupportedOperatingSystem: Optional[WindowsMinimumOperatingSystem] = Field(alias="minimumSupportedOperatingSystem", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_architecture import WindowsArchitecture
from .windows_minimum_operating_system import WindowsMinimumOperatingSystem
