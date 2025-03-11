from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceAndAppManagementAssignmentFilterCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[DeviceAndAppManagementAssignmentFilter]]] = Field(alias="value",default=None,)

from .device_and_app_management_assignment_filter import DeviceAndAppManagementAssignmentFilter

