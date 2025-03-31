from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeviceCompliancePolicyDeviceStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.deviceCompliancePolicyDeviceStateSummary"] = Field(alias="@odata.type",)
	compliantDeviceCount: Optional[int] = Field(alias="compliantDeviceCount", default=None,)
	configManagerCount: Optional[int] = Field(alias="configManagerCount", default=None,)
	conflictDeviceCount: Optional[int] = Field(alias="conflictDeviceCount", default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	inGracePeriodCount: Optional[int] = Field(alias="inGracePeriodCount", default=None,)
	nonCompliantDeviceCount: Optional[int] = Field(alias="nonCompliantDeviceCount", default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount", default=None,)
	remediatedDeviceCount: Optional[int] = Field(alias="remediatedDeviceCount", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)

