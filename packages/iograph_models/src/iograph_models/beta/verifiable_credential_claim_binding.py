from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiableCredentialClaimBinding(BaseModel):
	priority: Optional[int] = Field(alias="priority", default=None,)
	verifiableCredentialClaim: Optional[str] = Field(alias="verifiableCredentialClaim", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


