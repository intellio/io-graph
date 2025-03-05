from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RegistrationEnforcement(BaseModel):
	authenticationMethodsRegistrationCampaign: Optional[AuthenticationMethodsRegistrationCampaign] = Field(default=None,alias="authenticationMethodsRegistrationCampaign",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_methods_registration_campaign import AuthenticationMethodsRegistrationCampaign

