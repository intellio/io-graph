from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class M365AppsInstallationOptions(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.m365AppsInstallationOptions"] = Field(alias="@odata.type", default="#microsoft.graph.m365AppsInstallationOptions")
	appsForMac: Optional[AppsInstallationOptionsForMac] = Field(alias="appsForMac", default=None,)
	appsForWindows: Optional[AppsInstallationOptionsForWindows] = Field(alias="appsForWindows", default=None,)
	updateChannel: Optional[AppsUpdateChannelType | str] = Field(alias="updateChannel", default=None,)

from .apps_installation_options_for_mac import AppsInstallationOptionsForMac
from .apps_installation_options_for_windows import AppsInstallationOptionsForWindows
from .apps_update_channel_type import AppsUpdateChannelType
