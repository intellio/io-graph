from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class M365AppsInstallationOptions(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appsForMac: Optional[AppsInstallationOptionsForMac] = Field(alias="appsForMac",default=None,)
	appsForWindows: Optional[AppsInstallationOptionsForWindows] = Field(alias="appsForWindows",default=None,)
	updateChannel: Optional[str | AppsUpdateChannelType] = Field(alias="updateChannel",default=None,)

from .apps_installation_options_for_mac import AppsInstallationOptionsForMac
from .apps_installation_options_for_windows import AppsInstallationOptionsForWindows
from .apps_update_channel_type import AppsUpdateChannelType

