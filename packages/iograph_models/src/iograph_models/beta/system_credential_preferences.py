from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SystemCredentialPreferences(BaseModel):
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	includeTargets: Optional[list[IncludeTarget]] = Field(alias="includeTargets", default=None,)
	state: Optional[AdvancedConfigState | str] = Field(alias="state", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .exclude_target import ExcludeTarget
from .include_target import IncludeTarget
from .advanced_config_state import AdvancedConfigState
