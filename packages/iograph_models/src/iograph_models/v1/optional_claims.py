from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OptionalClaims(BaseModel):
	accessToken: Optional[list[OptionalClaim]] = Field(alias="accessToken",default=None,)
	idToken: Optional[list[OptionalClaim]] = Field(alias="idToken",default=None,)
	saml2Token: Optional[list[OptionalClaim]] = Field(alias="saml2Token",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .optional_claim import OptionalClaim
from .optional_claim import OptionalClaim
from .optional_claim import OptionalClaim

