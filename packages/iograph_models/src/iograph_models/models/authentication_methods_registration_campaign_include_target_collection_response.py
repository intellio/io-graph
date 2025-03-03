from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationMethodsRegistrationCampaignIncludeTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AuthenticationMethodsRegistrationCampaignIncludeTarget]] = Field(default=None,alias="value",)

from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget

