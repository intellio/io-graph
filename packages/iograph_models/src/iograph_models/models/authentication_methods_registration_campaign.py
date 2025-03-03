from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationMethodsRegistrationCampaign(BaseModel):
	excludeTargets: Optional[list[ExcludeTarget]] = Field(default=None,alias="excludeTargets",)
	includeTargets: Optional[list[AuthenticationMethodsRegistrationCampaignIncludeTarget]] = Field(default=None,alias="includeTargets",)
	snoozeDurationInDays: Optional[int] = Field(default=None,alias="snoozeDurationInDays",)
	state: Optional[AdvancedConfigState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .exclude_target import ExcludeTarget
from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget
from .advanced_config_state import AdvancedConfigState

