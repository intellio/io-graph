from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConditionalAccessEnumeratedExternalTenants(BaseModel):
	membershipKind: Optional[ConditionalAccessExternalTenantsMembershipKind] = Field(default=None,alias="membershipKind",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	members: Optional[list[str]] = Field(default=None,alias="members",)

from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind

