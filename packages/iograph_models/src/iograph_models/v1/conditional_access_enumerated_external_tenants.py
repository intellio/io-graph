from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ConditionalAccessEnumeratedExternalTenants(BaseModel):
	membershipKind: Optional[ConditionalAccessExternalTenantsMembershipKind | str] = Field(alias="membershipKind", default=None,)
	odata_type: Literal["#microsoft.graph.conditionalAccessEnumeratedExternalTenants"] = Field(alias="@odata.type", default="#microsoft.graph.conditionalAccessEnumeratedExternalTenants")
	members: Optional[list[str]] = Field(alias="members", default=None,)

from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind
