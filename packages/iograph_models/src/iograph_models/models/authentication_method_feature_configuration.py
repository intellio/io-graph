from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationMethodFeatureConfiguration(BaseModel):
	excludeTarget: Optional[FeatureTarget] = Field(default=None,alias="excludeTarget",)
	includeTarget: Optional[FeatureTarget] = Field(default=None,alias="includeTarget",)
	state: Optional[AdvancedConfigState] = Field(default=None,alias="state",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .feature_target import FeatureTarget
from .feature_target import FeatureTarget
from .advanced_config_state import AdvancedConfigState

