from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityVmMetadata(BaseModel):
	cloudProvider: Optional[SecurityVmCloudProvider | str] = Field(alias="cloudProvider",default=None,)
	resourceId: Optional[str] = Field(alias="resourceId",default=None,)
	subscriptionId: Optional[str] = Field(alias="subscriptionId",default=None,)
	vmId: Optional[str] = Field(alias="vmId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_vm_cloud_provider import SecurityVmCloudProvider

