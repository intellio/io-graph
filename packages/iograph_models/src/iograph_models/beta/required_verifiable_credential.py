from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RequiredVerifiableCredential(BaseModel):
	claimBindings: Optional[list[VerifiableCredentialClaimBinding]] = Field(alias="claimBindings",default=None,)
	trustedIssuer: Optional[str] = Field(alias="trustedIssuer",default=None,)
	verifiableCredentialType: Optional[str] = Field(alias="verifiableCredentialType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .verifiable_credential_claim_binding import VerifiableCredentialClaimBinding

