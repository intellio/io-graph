from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsDriverUpdateProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	approvalType: Optional[DriverUpdateProfileApprovalType | str] = Field(alias="approvalType", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deploymentDeferralInDays: Optional[int] = Field(alias="deploymentDeferralInDays", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	deviceReporting: Optional[int] = Field(alias="deviceReporting", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	inventorySyncStatus: Optional[WindowsDriverUpdateProfileInventorySyncStatus] = Field(alias="inventorySyncStatus", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	newUpdates: Optional[int] = Field(alias="newUpdates", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	assignments: Optional[list[WindowsDriverUpdateProfileAssignment]] = Field(alias="assignments", default=None,)
	driverInventories: Optional[list[WindowsDriverUpdateInventory]] = Field(alias="driverInventories", default=None,)

from .driver_update_profile_approval_type import DriverUpdateProfileApprovalType
from .windows_driver_update_profile_inventory_sync_status import WindowsDriverUpdateProfileInventorySyncStatus
from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
from .windows_driver_update_inventory import WindowsDriverUpdateInventory

