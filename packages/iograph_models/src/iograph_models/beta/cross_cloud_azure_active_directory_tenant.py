from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class CrossCloudAzureActiveDirectoryTenant(BaseModel):
	odata_type: Literal["#microsoft.graph.crossCloudAzureActiveDirectoryTenant"] = Field(alias="@odata.type", default="#microsoft.graph.crossCloudAzureActiveDirectoryTenant")
	cloudInstance: Optional[str] = Field(alias="cloudInstance", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)


