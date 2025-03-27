from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceOwnerKioskModeManagedFolderCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidDeviceOwnerKioskModeManagedFolder]] = Field(alias="value", default=None,)

from .android_device_owner_kiosk_mode_managed_folder import AndroidDeviceOwnerKioskModeManagedFolder

