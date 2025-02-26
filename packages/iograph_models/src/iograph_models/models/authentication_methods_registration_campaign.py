from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationMethodsRegistrationCampaign(BaseModel):
	excludeTargets: list[ExcludeTarget] = Field(alias="excludeTargets",)
	includeTargets: list[AuthenticationMethodsRegistrationCampaignIncludeTarget] = Field(alias="includeTargets",)
	snoozeDurationInDays: Optional[int] = Field(default=None,alias="snoozeDurationInDays",)
	state: Optional[AdvancedConfigState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .exclude_target import ExcludeTarget
from .authentication_methods_registration_campaign_include_target import AuthenticationMethodsRegistrationCampaignIncludeTarget
from .advanced_config_state import AdvancedConfigState

