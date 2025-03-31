from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AndroidDeviceOwnerKioskModeManagedFolder(BaseModel):
	folderIdentifier: Optional[str] = Field(alias="folderIdentifier", default=None,)
	folderName: Optional[str] = Field(alias="folderName", default=None,)
	items: Optional[list[Annotated[Union[AndroidDeviceOwnerKioskModeApp, AndroidDeviceOwnerKioskModeWeblink],Field(discriminator="odata_type")]]] = Field(alias="items", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink
