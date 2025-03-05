from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class M365AppsInstallationOptions(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appsForMac: Optional[AppsInstallationOptionsForMac] = Field(default=None,alias="appsForMac",)
	appsForWindows: Optional[AppsInstallationOptionsForWindows] = Field(default=None,alias="appsForWindows",)
	updateChannel: Optional[AppsUpdateChannelType] = Field(default=None,alias="updateChannel",)

from .apps_installation_options_for_mac import AppsInstallationOptionsForMac
from .apps_installation_options_for_windows import AppsInstallationOptionsForWindows
from .apps_update_channel_type import AppsUpdateChannelType

