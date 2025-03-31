from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsTenantCustomizedInformation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.tenantCustomizedInformation"] = Field(alias="@odata.type",)
	businessRelationship: Optional[str] = Field(alias="businessRelationship", default=None,)
	complianceRequirements: Optional[list[str]] = Field(alias="complianceRequirements", default=None,)
	contacts: Optional[list[ManagedTenantsTenantContactInformation]] = Field(alias="contacts", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	managedServicesPlans: Optional[list[str]] = Field(alias="managedServicesPlans", default=None,)
	note: Optional[str] = Field(alias="note", default=None,)
	noteLastModifiedDateTime: Optional[datetime] = Field(alias="noteLastModifiedDateTime", default=None,)
	partnerRelationshipManagerUserIds: Optional[list[str]] = Field(alias="partnerRelationshipManagerUserIds", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	website: Optional[str] = Field(alias="website", default=None,)

from .managed_tenants_tenant_contact_information import ManagedTenantsTenantContactInformation
