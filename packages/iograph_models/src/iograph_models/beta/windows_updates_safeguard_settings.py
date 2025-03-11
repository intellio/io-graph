from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesSafeguardSettings(BaseModel):
	disabledSafeguardProfiles: Optional[list[WindowsUpdatesSafeguardProfile]] = Field(alias="disabledSafeguardProfiles",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .windows_updates_safeguard_profile import WindowsUpdatesSafeguardProfile

