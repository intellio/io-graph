from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CrossCloudAzureActiveDirectoryTenant(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cloudInstance: Optional[str] = Field(alias="cloudInstance",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)


