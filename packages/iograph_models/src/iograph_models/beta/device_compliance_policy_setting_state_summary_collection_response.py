from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceCompliancePolicySettingStateSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[DeviceCompliancePolicySettingStateSummary]] = Field(alias="value",default=None,)

from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary

