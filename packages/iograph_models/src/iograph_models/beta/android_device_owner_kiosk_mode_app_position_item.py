from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AndroidDeviceOwnerKioskModeAppPositionItem(BaseModel):
	item: Optional[Union[AndroidDeviceOwnerKioskModeApp, AndroidDeviceOwnerKioskModeWeblink, AndroidDeviceOwnerKioskModeManagedFolderReference]] = Field(alias="item", default=None,discriminator="odata_type", )
	position: Optional[int] = Field(alias="position", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .android_device_owner_kiosk_mode_app import AndroidDeviceOwnerKioskModeApp
from .android_device_owner_kiosk_mode_weblink import AndroidDeviceOwnerKioskModeWeblink
from .android_device_owner_kiosk_mode_managed_folder_reference import AndroidDeviceOwnerKioskModeManagedFolderReference
