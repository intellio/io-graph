from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TenantRelationshipAccessPolicyBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[TenantRelationshipAccessPolicyBase]]] = Field(alias="value",default=None,)

from .tenant_relationship_access_policy_base import TenantRelationshipAccessPolicyBase

