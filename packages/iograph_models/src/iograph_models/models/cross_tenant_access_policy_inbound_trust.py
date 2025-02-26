from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyInboundTrust(BaseModel):
	isCompliantDeviceAccepted: Optional[bool] = Field(default=None,alias="isCompliantDeviceAccepted",)
	isHybridAzureADJoinedDeviceAccepted: Optional[bool] = Field(default=None,alias="isHybridAzureADJoinedDeviceAccepted",)
	isMfaAccepted: Optional[bool] = Field(default=None,alias="isMfaAccepted",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


