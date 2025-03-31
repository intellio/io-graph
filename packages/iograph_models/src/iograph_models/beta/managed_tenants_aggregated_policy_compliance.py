from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsAggregatedPolicyCompliance(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.aggregatedPolicyCompliance"] = Field(alias="@odata.type",)
	compliancePolicyId: Optional[str] = Field(alias="compliancePolicyId", default=None,)
	compliancePolicyName: Optional[str] = Field(alias="compliancePolicyName", default=None,)
	compliancePolicyPlatform: Optional[str] = Field(alias="compliancePolicyPlatform", default=None,)
	compliancePolicyType: Optional[str] = Field(alias="compliancePolicyType", default=None,)
	lastRefreshedDateTime: Optional[datetime] = Field(alias="lastRefreshedDateTime", default=None,)
	numberOfCompliantDevices: Optional[int] = Field(alias="numberOfCompliantDevices", default=None,)
	numberOfErrorDevices: Optional[int] = Field(alias="numberOfErrorDevices", default=None,)
	numberOfNonCompliantDevices: Optional[int] = Field(alias="numberOfNonCompliantDevices", default=None,)
	policyModifiedDateTime: Optional[datetime] = Field(alias="policyModifiedDateTime", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)

