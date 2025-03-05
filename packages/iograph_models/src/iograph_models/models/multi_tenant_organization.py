from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MultiTenantOrganization(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	state: Optional[MultiTenantOrganizationState] = Field(default=None,alias="state",)
	joinRequest: Optional[MultiTenantOrganizationJoinRequestRecord] = Field(default=None,alias="joinRequest",)
	tenants: Optional[list[MultiTenantOrganizationMember]] = Field(default=None,alias="tenants",)

from .multi_tenant_organization_state import MultiTenantOrganizationState
from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
from .multi_tenant_organization_member import MultiTenantOrganizationMember

