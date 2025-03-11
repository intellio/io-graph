from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsTenantInfo(BaseModel):
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


