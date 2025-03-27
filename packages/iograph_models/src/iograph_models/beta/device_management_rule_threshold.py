from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementRuleThreshold(BaseModel):
	aggregation: Optional[DeviceManagementAggregationType | str] = Field(alias="aggregation", default=None,)
	operator: Optional[DeviceManagementOperatorType | str] = Field(alias="operator", default=None,)
	target: Optional[int] = Field(alias="target", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_aggregation_type import DeviceManagementAggregationType
from .device_management_operator_type import DeviceManagementOperatorType

