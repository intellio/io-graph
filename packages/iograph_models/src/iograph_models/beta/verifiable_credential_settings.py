from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialSettings(BaseModel):
	credentialTypes: Optional[list[VerifiableCredentialType]] = Field(alias="credentialTypes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .verifiable_credential_type import VerifiableCredentialType

