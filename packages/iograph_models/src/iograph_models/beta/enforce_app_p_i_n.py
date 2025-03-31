from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EnforceAppPIN(BaseModel):
	excludeTargets: Optional[list[ExcludeTarget]] = Field(alias="excludeTargets", default=None,)
	includeTargets: Optional[list[IncludeTarget]] = Field(alias="includeTargets", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .exclude_target import ExcludeTarget
from .include_target import IncludeTarget
