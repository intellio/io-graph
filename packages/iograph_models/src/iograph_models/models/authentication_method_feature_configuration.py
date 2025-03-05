from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodFeatureConfiguration(BaseModel):
	excludeTarget: Optional[FeatureTarget] = Field(alias="excludeTarget",default=None,)
	includeTarget: Optional[FeatureTarget] = Field(alias="includeTarget",default=None,)
	state: Optional[str | AdvancedConfigState] = Field(alias="state",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .feature_target import FeatureTarget
from .feature_target import FeatureTarget
from .advanced_config_state import AdvancedConfigState

