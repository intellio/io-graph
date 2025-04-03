from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class AuthenticationStrengthPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.authenticationStrengthPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.authenticationStrengthPolicy")
	allowedCombinations: Optional[list[AuthenticationMethodModes | str]] = Field(alias="allowedCombinations", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	policyType: Optional[AuthenticationStrengthPolicyType | str] = Field(alias="policyType", default=None,)
	requirementsSatisfied: Optional[AuthenticationStrengthRequirements | str] = Field(alias="requirementsSatisfied", default=None,)
	combinationConfigurations: Optional[list[Annotated[Union[Fido2CombinationConfiguration, X509CertificateCombinationConfiguration],Field(discriminator="odata_type")]]] = Field(alias="combinationConfigurations", default=None,)

from .authentication_method_modes import AuthenticationMethodModes
from .authentication_strength_policy_type import AuthenticationStrengthPolicyType
from .authentication_strength_requirements import AuthenticationStrengthRequirements
from .fido2_combination_configuration import Fido2CombinationConfiguration
from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration
