from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalLockConfiguration(BaseModel):
	allProperties: Optional[bool] = Field(default=None,alias="allProperties",)
	credentialsWithUsageSign: Optional[bool] = Field(default=None,alias="credentialsWithUsageSign",)
	credentialsWithUsageVerify: Optional[bool] = Field(default=None,alias="credentialsWithUsageVerify",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	tokenEncryptionKeyId: Optional[bool] = Field(default=None,alias="tokenEncryptionKeyId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


