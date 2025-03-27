from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUserExperienceSettings(BaseModel):
	daysUntilForcedReboot: Optional[int] = Field(alias="daysUntilForcedReboot", default=None,)
	isHotpatchEnabled: Optional[bool] = Field(alias="isHotpatchEnabled", default=None,)
	offerAsOptional: Optional[bool] = Field(alias="offerAsOptional", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


