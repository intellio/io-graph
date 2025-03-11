from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesAzureADDevice(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	enrollment: Optional[WindowsUpdatesUpdateManagementEnrollment] = Field(alias="enrollment",default=None,)
	errors: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAssetError]]] = Field(alias="errors",default=None,)

from .windows_updates_update_management_enrollment import WindowsUpdatesUpdateManagementEnrollment
from .windows_updates_updatable_asset_error import WindowsUpdatesUpdatableAssetError

