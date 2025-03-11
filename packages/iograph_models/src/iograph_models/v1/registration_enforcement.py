from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RegistrationEnforcement(BaseModel):
	authenticationMethodsRegistrationCampaign: Optional[AuthenticationMethodsRegistrationCampaign] = Field(alias="authenticationMethodsRegistrationCampaign",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_methods_registration_campaign import AuthenticationMethodsRegistrationCampaign

