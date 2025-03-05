from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossCloudAzureActiveDirectoryTenant(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	cloudInstance: Optional[str] = Field(default=None,alias="cloudInstance",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)


