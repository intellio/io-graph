from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementEnumConstraint(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	values: Optional[list[DeviceManagementEnumValue]] = Field(alias="values",default=None,)

from .device_management_enum_value import DeviceManagementEnumValue

