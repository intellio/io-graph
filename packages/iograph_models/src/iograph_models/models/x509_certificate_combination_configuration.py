from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class X509CertificateCombinationConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appliesToCombinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="appliesToCombinations",default=None,)
	allowedIssuerSkis: Optional[list[str]] = Field(alias="allowedIssuerSkis",default=None,)
	allowedPolicyOIDs: Optional[list[str]] = Field(alias="allowedPolicyOIDs",default=None,)

from .authentication_method_modes import AuthenticationMethodModes

