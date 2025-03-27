from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PayloadByFilter(BaseModel):
	assignmentFilterType: Optional[DeviceAndAppManagementAssignmentFilterType | str] = Field(alias="assignmentFilterType", default=None,)
	groupId: Optional[str] = Field(alias="groupId", default=None,)
	payloadId: Optional[str] = Field(alias="payloadId", default=None,)
	payloadType: Optional[AssociatedAssignmentPayloadType | str] = Field(alias="payloadType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_and_app_management_assignment_filter_type import DeviceAndAppManagementAssignmentFilterType
from .associated_assignment_payload_type import AssociatedAssignmentPayloadType

