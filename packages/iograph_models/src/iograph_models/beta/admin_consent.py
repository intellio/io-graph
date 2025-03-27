from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AdminConsent(BaseModel):
	shareAPNSData: Optional[AdminConsentState | str] = Field(alias="shareAPNSData", default=None,)
	shareUserExperienceAnalyticsData: Optional[AdminConsentState | str] = Field(alias="shareUserExperienceAnalyticsData", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .admin_consent_state import AdminConsentState
from .admin_consent_state import AdminConsentState

