from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MultiTenantOrganization(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.multiTenantOrganization"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	state: Optional[MultiTenantOrganizationState | str] = Field(alias="state", default=None,)
	joinRequest: Optional[MultiTenantOrganizationJoinRequestRecord] = Field(alias="joinRequest", default=None,)
	tenants: Optional[list[MultiTenantOrganizationMember]] = Field(alias="tenants", default=None,)

from .multi_tenant_organization_state import MultiTenantOrganizationState
from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
from .multi_tenant_organization_member import MultiTenantOrganizationMember
