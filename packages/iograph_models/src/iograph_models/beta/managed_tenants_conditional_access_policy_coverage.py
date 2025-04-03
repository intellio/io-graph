from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsConditionalAccessPolicyCoverage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.conditionalAccessPolicyCoverage"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.conditionalAccessPolicyCoverage")
	conditionalAccessPolicyState: Optional[str] = Field(alias="conditionalAccessPolicyState", default=None,)
	latestPolicyModifiedDateTime: Optional[datetime] = Field(alias="latestPolicyModifiedDateTime", default=None,)
	requiresDeviceCompliance: Optional[bool] = Field(alias="requiresDeviceCompliance", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)

