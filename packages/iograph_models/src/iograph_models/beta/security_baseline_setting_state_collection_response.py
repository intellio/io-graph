from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityBaselineSettingStateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityBaselineSettingState]] = Field(alias="value", default=None,)

from .security_baseline_setting_state import SecurityBaselineSettingState
