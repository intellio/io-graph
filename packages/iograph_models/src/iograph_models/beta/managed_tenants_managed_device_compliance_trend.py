from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ManagedTenantsManagedDeviceComplianceTrend(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedDeviceComplianceTrend"] = Field(alias="@odata.type",)
	compliantDeviceCount: Optional[int] = Field(alias="compliantDeviceCount", default=None,)
	configManagerDeviceCount: Optional[int] = Field(alias="configManagerDeviceCount", default=None,)
	countDateTime: Optional[str] = Field(alias="countDateTime", default=None,)
	errorDeviceCount: Optional[int] = Field(alias="errorDeviceCount", default=None,)
	inGracePeriodDeviceCount: Optional[int] = Field(alias="inGracePeriodDeviceCount", default=None,)
	noncompliantDeviceCount: Optional[int] = Field(alias="noncompliantDeviceCount", default=None,)
	tenantDisplayName: Optional[str] = Field(alias="tenantDisplayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	unknownDeviceCount: Optional[int] = Field(alias="unknownDeviceCount", default=None,)

