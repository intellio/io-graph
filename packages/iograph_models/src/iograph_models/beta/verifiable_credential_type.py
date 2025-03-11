from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialType(BaseModel):
	credentialType: Optional[str] = Field(alias="credentialType",default=None,)
	issuers: Optional[list[str]] = Field(alias="issuers",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


