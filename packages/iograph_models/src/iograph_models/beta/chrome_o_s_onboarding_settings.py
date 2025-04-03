from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ChromeOSOnboardingSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.chromeOSOnboardingSettings"] = Field(alias="@odata.type", default="#microsoft.graph.chromeOSOnboardingSettings")
	lastDirectorySyncDateTime: Optional[datetime] = Field(alias="lastDirectorySyncDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	onboardingStatus: Optional[OnboardingStatus | str] = Field(alias="onboardingStatus", default=None,)
	ownerUserPrincipalName: Optional[str] = Field(alias="ownerUserPrincipalName", default=None,)

from .onboarding_status import OnboardingStatus
