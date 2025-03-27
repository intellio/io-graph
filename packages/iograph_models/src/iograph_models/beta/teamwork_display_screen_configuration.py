from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkDisplayScreenConfiguration(BaseModel):
	backlightBrightness: Optional[int] = Field(alias="backlightBrightness", default=None,)
	backlightTimeout: Optional[str] = Field(alias="backlightTimeout", default=None,)
	isHighContrastEnabled: Optional[bool] = Field(alias="isHighContrastEnabled", default=None,)
	isScreensaverEnabled: Optional[bool] = Field(alias="isScreensaverEnabled", default=None,)
	screensaverTimeout: Optional[str] = Field(alias="screensaverTimeout", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


