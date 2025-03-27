from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesContentApplicabilitySettings(BaseModel):
	offerWhileRecommendedBy: Optional[list[str]] = Field(alias="offerWhileRecommendedBy", default=None,)
	safeguard: Optional[WindowsUpdatesSafeguardSettings] = Field(alias="safeguard", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .windows_updates_safeguard_settings import WindowsUpdatesSafeguardSettings

