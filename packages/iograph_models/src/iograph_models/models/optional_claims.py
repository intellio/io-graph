from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OptionalClaims(BaseModel):
	accessToken: list[OptionalClaim] = Field(alias="accessToken",)
	idToken: list[OptionalClaim] = Field(alias="idToken",)
	saml2Token: list[OptionalClaim] = Field(alias="saml2Token",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .optional_claim import OptionalClaim
from .optional_claim import OptionalClaim
from .optional_claim import OptionalClaim

