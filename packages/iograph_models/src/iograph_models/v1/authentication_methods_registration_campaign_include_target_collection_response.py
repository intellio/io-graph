from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsRegistrationCampaignIncludeTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AuthenticationMethodsRegistrationCampaignIncludeTarget]] = Field(alias="value", default=None,)

from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget

