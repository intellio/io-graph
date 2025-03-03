from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OptionalClaims(BaseModel):
	accessToken: Optional[list[OptionalClaim]] = Field(default=None,alias="accessToken",)
	idToken: Optional[list[OptionalClaim]] = Field(default=None,alias="idToken",)
	saml2Token: Optional[list[OptionalClaim]] = Field(default=None,alias="saml2Token",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .optional_claim import OptionalClaim
from .optional_claim import OptionalClaim
from .optional_claim import OptionalClaim

