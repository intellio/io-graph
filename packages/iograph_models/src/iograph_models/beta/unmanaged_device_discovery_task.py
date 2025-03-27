from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UnmanagedDeviceDiscoveryTask(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unmanagedDeviceDiscoveryTask"] = Field(alias="@odata.type", default="#microsoft.graph.unmanagedDeviceDiscoveryTask")
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	category: Optional[DeviceAppManagementTaskCategory | str] = Field(alias="category", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	creator: Optional[str] = Field(alias="creator", default=None,)
	creatorNotes: Optional[str] = Field(alias="creatorNotes", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	dueDateTime: Optional[datetime] = Field(alias="dueDateTime", default=None,)
	priority: Optional[DeviceAppManagementTaskPriority | str] = Field(alias="priority", default=None,)
	status: Optional[DeviceAppManagementTaskStatus | str] = Field(alias="status", default=None,)
	unmanagedDevices: Optional[list[UnmanagedDevice]] = Field(alias="unmanagedDevices", default=None,)

from .device_app_management_task_category import DeviceAppManagementTaskCategory
from .device_app_management_task_priority import DeviceAppManagementTaskPriority
from .device_app_management_task_status import DeviceAppManagementTaskStatus
from .unmanaged_device import UnmanagedDevice

