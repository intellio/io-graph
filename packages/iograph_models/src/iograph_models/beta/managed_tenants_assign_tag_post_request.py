from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Managed_tenants_assign_tagPostRequest(BaseModel):
	tenantIds: Optional[list[str]] = Field(alias="tenantIds",default=None,)


