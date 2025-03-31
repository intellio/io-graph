from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomAppSettings(BaseModel):
	developerToolsForShowingAppUsageMetrics: Optional[AppDevelopmentPlatforms | str] = Field(alias="developerToolsForShowingAppUsageMetrics", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .app_development_platforms import AppDevelopmentPlatforms
