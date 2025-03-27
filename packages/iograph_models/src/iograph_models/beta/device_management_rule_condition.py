from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementRuleCondition(BaseModel):
	aggregation: Optional[DeviceManagementAggregationType | str] = Field(alias="aggregation", default=None,)
	conditionCategory: Optional[DeviceManagementConditionCategory | str] = Field(alias="conditionCategory", default=None,)
	operator: Optional[DeviceManagementOperatorType | str] = Field(alias="operator", default=None,)
	relationshipType: Optional[DeviceManagementRelationshipType | str] = Field(alias="relationshipType", default=None,)
	thresholdValue: Optional[str] = Field(alias="thresholdValue", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_aggregation_type import DeviceManagementAggregationType
from .device_management_condition_category import DeviceManagementConditionCategory
from .device_management_operator_type import DeviceManagementOperatorType
from .device_management_relationship_type import DeviceManagementRelationshipType

