from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExpeditedWindowsQualityUpdateSettings(BaseModel):
	daysUntilForcedReboot: Optional[int] = Field(alias="daysUntilForcedReboot", default=None,)
	qualityUpdateRelease: Optional[str] = Field(alias="qualityUpdateRelease", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


