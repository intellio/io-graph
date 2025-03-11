from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingDependency(BaseModel):
	constraints: SerializeAsAny[Optional[list[DeviceManagementConstraint]]] = Field(alias="constraints",default=None,)
	definitionId: Optional[str] = Field(alias="definitionId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_constraint import DeviceManagementConstraint

