from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsDeviceCompliancePolicySettingStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.deviceCompliancePolicySettingStateSummary"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.deviceCompliancePolicySettingStateSummary")
	conflictDeviceCount: Optional[int] = Field(alias="conflictDeviceCount", default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	failedDeviceCount: Optional[int] = Field(alias="failedDeviceCount", default=None,)
	intuneAccountId: Optional[str] = Field(alias="intuneAccountId", default=None,)
	intuneSettingId: Optional[str] = Field(alias="intuneSettingId", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	notApplicableDeviceCount: Optional[int] = Field(alias="notApplicableDeviceCount", default=None,)
	pendingDeviceCount: Optional[int] = Field(alias="pendingDeviceCount", default=None,)
	policyType: Optional[str] = Field(alias="policyType", default=None,)
	settingName: Optional[str] = Field(alias="settingName", default=None,)
	succeededDeviceCount: Optional[int] = Field(alias="succeededDeviceCount", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

