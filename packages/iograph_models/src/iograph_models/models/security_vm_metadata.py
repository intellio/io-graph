from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityVmMetadata(BaseModel):
	cloudProvider: Optional[SecurityVmCloudProvider] = Field(default=None,alias="cloudProvider",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	subscriptionId: Optional[str] = Field(default=None,alias="subscriptionId",)
	vmId: Optional[str] = Field(default=None,alias="vmId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_vm_cloud_provider import SecurityVmCloudProvider

