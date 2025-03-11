from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Managed_tenants_tenant_searchPostRequest(BaseModel):
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)


