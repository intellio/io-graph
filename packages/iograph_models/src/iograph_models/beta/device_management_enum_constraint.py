from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementEnumConstraint(BaseModel):
	odata_type: Literal["#microsoft.graph.deviceManagementEnumConstraint"] = Field(alias="@odata.type", default="#microsoft.graph.deviceManagementEnumConstraint")
	values: Optional[list[DeviceManagementEnumValue]] = Field(alias="values", default=None,)

from .device_management_enum_value import DeviceManagementEnumValue

