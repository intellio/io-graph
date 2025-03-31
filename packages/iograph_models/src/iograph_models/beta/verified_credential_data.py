from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VerifiedCredentialData(BaseModel):
	authority: Optional[str] = Field(alias="authority", default=None,)
	claims: Optional[VerifiedCredentialClaims] = Field(alias="claims", default=None,)
	type: Optional[list[str]] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .verified_credential_claims import VerifiedCredentialClaims
