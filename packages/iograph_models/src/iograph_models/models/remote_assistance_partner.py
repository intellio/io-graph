from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class RemoteAssistancePartner(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastConnectionDateTime: Optional[datetime] = Field(default=None,alias="lastConnectionDateTime",)
	onboardingStatus: Optional[RemoteAssistanceOnboardingStatus] = Field(default=None,alias="onboardingStatus",)
	onboardingUrl: Optional[str] = Field(default=None,alias="onboardingUrl",)

from .remote_assistance_onboarding_status import RemoteAssistanceOnboardingStatus

