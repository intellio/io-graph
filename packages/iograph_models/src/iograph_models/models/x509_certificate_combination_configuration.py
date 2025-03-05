from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateCombinationConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appliesToCombinations: Optional[list[AuthenticationMethodModes]] = Field(default=None,alias="appliesToCombinations",)
	allowedIssuerSkis: Optional[list[str]] = Field(default=None,alias="allowedIssuerSkis",)
	allowedPolicyOIDs: Optional[list[str]] = Field(default=None,alias="allowedPolicyOIDs",)

from .authentication_method_modes import AuthenticationMethodModes

