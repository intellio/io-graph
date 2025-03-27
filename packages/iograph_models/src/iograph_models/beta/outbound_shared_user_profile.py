from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutboundSharedUserProfile(BaseModel):
	userId: Optional[str] = Field(alias="userId", default=None,)
	tenants: Optional[list[TenantReference]] = Field(alias="tenants", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .tenant_reference import TenantReference

