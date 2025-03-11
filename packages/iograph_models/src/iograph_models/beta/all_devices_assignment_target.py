from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AllDevicesAssignmentTarget(BaseModel):
	deviceAndAppManagementAssignmentFilterId: Optional[str] = Field(alias="deviceAndAppManagementAssignmentFilterId",default=None,)
	deviceAndAppManagementAssignmentFilterType: Optional[DeviceAndAppManagementAssignmentFilterType | str] = Field(alias="deviceAndAppManagementAssignmentFilterType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType

