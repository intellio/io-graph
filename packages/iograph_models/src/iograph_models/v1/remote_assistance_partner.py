from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class RemoteAssistancePartner(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.remoteAssistancePartner"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastConnectionDateTime: Optional[datetime] = Field(alias="lastConnectionDateTime", default=None,)
	onboardingStatus: Optional[RemoteAssistanceOnboardingStatus | str] = Field(alias="onboardingStatus", default=None,)
	onboardingUrl: Optional[str] = Field(alias="onboardingUrl", default=None,)

from .remote_assistance_onboarding_status import RemoteAssistanceOnboardingStatus
