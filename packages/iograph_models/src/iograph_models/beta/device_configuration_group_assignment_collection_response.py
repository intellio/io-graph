from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceConfigurationGroupAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DeviceConfigurationGroupAssignment]] = Field(alias="value", default=None,)

from .device_configuration_group_assignment import DeviceConfigurationGroupAssignment
