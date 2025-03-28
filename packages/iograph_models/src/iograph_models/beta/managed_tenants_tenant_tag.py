from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsTenantTag(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	tenants: Optional[list[ManagedTenantsTenantInfo]] = Field(alias="tenants", default=None,)

from .managed_tenants_tenant_info import ManagedTenantsTenantInfo

