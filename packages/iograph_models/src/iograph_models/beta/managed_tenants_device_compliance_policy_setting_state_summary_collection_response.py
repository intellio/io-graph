from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsDeviceCompliancePolicySettingStateSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ManagedTenantsDeviceCompliancePolicySettingStateSummary]] = Field(alias="value", default=None,)

from .managed_tenants_device_compliance_policy_setting_state_summary import ManagedTenantsDeviceCompliancePolicySettingStateSummary

