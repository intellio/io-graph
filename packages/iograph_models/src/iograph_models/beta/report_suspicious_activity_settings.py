from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReportSuspiciousActivitySettings(BaseModel):
	includeTarget: Optional[IncludeTarget] = Field(alias="includeTarget", default=None,)
	state: Optional[AdvancedConfigState | str] = Field(alias="state", default=None,)
	voiceReportingCode: Optional[int] = Field(alias="voiceReportingCode", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .include_target import IncludeTarget
from .advanced_config_state import AdvancedConfigState
