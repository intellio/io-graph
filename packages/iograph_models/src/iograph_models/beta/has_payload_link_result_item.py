from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class HasPayloadLinkResultItem(BaseModel):
	error: Optional[str] = Field(alias="error",default=None,)
	hasLink: Optional[bool] = Field(alias="hasLink",default=None,)
	payloadId: Optional[str] = Field(alias="payloadId",default=None,)
	sources: Optional[list[DeviceAndAppManagementAssignmentSource | str]] = Field(alias="sources",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_and_app_management_assignment_source import DeviceAndAppManagementAssignmentSource

