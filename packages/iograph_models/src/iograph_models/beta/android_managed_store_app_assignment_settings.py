from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidManagedStoreAppAssignmentSettings(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	androidManagedStoreAppTrackIds: Optional[list[str]] = Field(alias="androidManagedStoreAppTrackIds",default=None,)
	autoUpdateMode: Optional[AndroidManagedStoreAutoUpdateMode | str] = Field(alias="autoUpdateMode",default=None,)

from .android_managed_store_auto_update_mode import AndroidManagedStoreAutoUpdateMode

