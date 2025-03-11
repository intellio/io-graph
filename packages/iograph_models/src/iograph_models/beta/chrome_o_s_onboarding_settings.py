from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChromeOSOnboardingSettings(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastDirectorySyncDateTime: Optional[datetime] = Field(alias="lastDirectorySyncDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	onboardingStatus: Optional[OnboardingStatus | str] = Field(alias="onboardingStatus",default=None,)
	ownerUserPrincipalName: Optional[str] = Field(alias="ownerUserPrincipalName",default=None,)

from .onboarding_status import OnboardingStatus

