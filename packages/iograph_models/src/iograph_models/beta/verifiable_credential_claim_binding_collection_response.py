from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialClaimBindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[VerifiableCredentialClaimBinding]] = Field(alias="value", default=None,)

from .verifiable_credential_claim_binding import VerifiableCredentialClaimBinding

