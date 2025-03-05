from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RemoteAssistancePartner(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastConnectionDateTime: Optional[datetime] = Field(alias="lastConnectionDateTime",default=None,)
	onboardingStatus: Optional[str | RemoteAssistanceOnboardingStatus] = Field(alias="onboardingStatus",default=None,)
	onboardingUrl: Optional[str] = Field(alias="onboardingUrl",default=None,)

from .remote_assistance_onboarding_status import RemoteAssistanceOnboardingStatus

