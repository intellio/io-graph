from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicySettingStateSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DeviceCompliancePolicySettingStateSummary]] = Field(default=None,alias="value",)

from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary

