from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementAlertImpact(BaseModel):
	aggregationType: Optional[DeviceManagementAggregationType | str] = Field(alias="aggregationType",default=None,)
	alertImpactDetails: Optional[list[KeyValuePair]] = Field(alias="alertImpactDetails",default=None,)
	value: Optional[int] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_aggregation_type import DeviceManagementAggregationType
from .key_value_pair import KeyValuePair

