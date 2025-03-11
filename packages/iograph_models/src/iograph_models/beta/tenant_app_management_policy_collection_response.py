from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TenantAppManagementPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[TenantAppManagementPolicy]] = Field(alias="value",default=None,)

from .tenant_app_management_policy import TenantAppManagementPolicy

