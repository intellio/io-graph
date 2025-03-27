from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsRegistrationCampaign(BaseModel):
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	includeTargets: Optional[list[AuthenticationMethodsRegistrationCampaignIncludeTarget]] = Field(alias="includeTargets", default=None,)
	snoozeDurationInDays: Optional[int] = Field(alias="snoozeDurationInDays", default=None,)
	state: Optional[AdvancedConfigState | str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .exclude_target import ExcludeTarget
from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget
from .advanced_config_state import AdvancedConfigState

