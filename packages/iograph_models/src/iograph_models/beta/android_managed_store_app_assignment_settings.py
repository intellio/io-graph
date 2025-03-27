from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidManagedStoreAppAssignmentSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.androidManagedStoreAppAssignmentSettings"] = Field(alias="@odata.type", default="#microsoft.graph.androidManagedStoreAppAssignmentSettings")
	androidManagedStoreAppTrackIds: Optional[list[str]] = Field(alias="androidManagedStoreAppTrackIds", default=None,)
	autoUpdateMode: Optional[AndroidManagedStoreAutoUpdateMode | str] = Field(alias="autoUpdateMode", default=None,)

from .android_managed_store_auto_update_mode import AndroidManagedStoreAutoUpdateMode

