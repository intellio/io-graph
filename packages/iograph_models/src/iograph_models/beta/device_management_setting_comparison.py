from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingComparison(BaseModel):
	comparisonResult: Optional[DeviceManagementComparisonResult | str] = Field(alias="comparisonResult", default=None,)
	currentValueJson: Optional[str] = Field(alias="currentValueJson", default=None,)
	definitionId: Optional[str] = Field(alias="definitionId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	newValueJson: Optional[str] = Field(alias="newValueJson", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_comparison_result import DeviceManagementComparisonResult

