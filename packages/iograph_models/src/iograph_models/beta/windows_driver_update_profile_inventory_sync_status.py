from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDriverUpdateProfileInventorySyncStatus(BaseModel):
	driverInventorySyncState: Optional[WindowsDriverUpdateProfileInventorySyncState | str] = Field(alias="driverInventorySyncState", default=None,)
	lastSuccessfulSyncDateTime: Optional[datetime] = Field(alias="lastSuccessfulSyncDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_driver_update_profile_inventory_sync_state import WindowsDriverUpdateProfileInventorySyncState

