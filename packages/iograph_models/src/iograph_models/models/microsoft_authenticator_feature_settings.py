from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftAuthenticatorFeatureSettings(BaseModel):
	displayAppInformationRequiredState: Optional[AuthenticationMethodFeatureConfiguration] = Field(default=None,alias="displayAppInformationRequiredState",)
	displayLocationInformationRequiredState: Optional[AuthenticationMethodFeatureConfiguration] = Field(default=None,alias="displayLocationInformationRequiredState",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_method_feature_configuration import AuthenticationMethodFeatureConfiguration
from .authentication_method_feature_configuration import AuthenticationMethodFeatureConfiguration

