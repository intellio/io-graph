from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessAllExternalTenants(BaseModel):
	membershipKind: Optional[ConditionalAccessExternalTenantsMembershipKind | str] = Field(alias="membershipKind", default=None,)
	odata_type: Literal["#microsoft.graph.conditionalAccessAllExternalTenants"] = Field(alias="@odata.type", default="#microsoft.graph.conditionalAccessAllExternalTenants")

from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind

