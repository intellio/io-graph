from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedDeviceMobileAppConfigurationAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedDeviceMobileAppConfigurationAssignment]] = Field(alias="value", default=None,)

from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
