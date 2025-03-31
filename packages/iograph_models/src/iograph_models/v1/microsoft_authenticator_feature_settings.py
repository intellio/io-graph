from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftAuthenticatorFeatureSettings(BaseModel):
	displayAppInformationRequiredState: Optional[AuthenticationMethodFeatureConfiguration] = Field(alias="displayAppInformationRequiredState", default=None,)
	displayLocationInformationRequiredState: Optional[AuthenticationMethodFeatureConfiguration] = Field(alias="displayLocationInformationRequiredState", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_method_feature_configuration import AuthenticationMethodFeatureConfiguration
