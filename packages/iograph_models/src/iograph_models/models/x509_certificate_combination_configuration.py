from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class X509CertificateCombinationConfiguration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appliesToCombinations: list[AuthenticationMethodModes] = Field(alias="appliesToCombinations",)
	allowedIssuerSkis: list[str] = Field(alias="allowedIssuerSkis",)
	allowedPolicyOIDs: list[str] = Field(alias="allowedPolicyOIDs",)

from .authentication_method_modes import AuthenticationMethodModes

