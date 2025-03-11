from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServicePrincipalLockConfiguration(BaseModel):
	allProperties: Optional[bool] = Field(alias="allProperties",default=None,)
	credentialsWithUsageSign: Optional[bool] = Field(alias="credentialsWithUsageSign",default=None,)
	credentialsWithUsageVerify: Optional[bool] = Field(alias="credentialsWithUsageVerify",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	tokenEncryptionKeyId: Optional[bool] = Field(alias="tokenEncryptionKeyId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


