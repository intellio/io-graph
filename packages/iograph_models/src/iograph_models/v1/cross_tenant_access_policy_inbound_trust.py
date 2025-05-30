from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CrossTenantAccessPolicyInboundTrust(BaseModel):
	isCompliantDeviceAccepted: Optional[bool] = Field(alias="isCompliantDeviceAccepted", default=None,)
	isHybridAzureADJoinedDeviceAccepted: Optional[bool] = Field(alias="isHybridAzureADJoinedDeviceAccepted", default=None,)
	isMfaAccepted: Optional[bool] = Field(alias="isMfaAccepted", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

