from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerKioskModeManagedFolder(BaseModel):
	folderIdentifier: Optional[str] = Field(alias="folderIdentifier",default=None,)
	folderName: Optional[str] = Field(alias="folderName",default=None,)
	items: SerializeAsAny[Optional[list[AndroidDeviceOwnerKioskModeFolderItem]]] = Field(alias="items",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .android_device_owner_kiosk_mode_folder_item import AndroidDeviceOwnerKioskModeFolderItem

