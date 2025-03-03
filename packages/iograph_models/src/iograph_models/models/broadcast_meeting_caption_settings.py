from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class BroadcastMeetingCaptionSettings(BaseModel):
	isCaptionEnabled: Optional[bool] = Field(default=None,alias="isCaptionEnabled",)
	spokenLanguage: Optional[str] = Field(default=None,alias="spokenLanguage",)
	translationLanguages: Optional[list[str]] = Field(default=None,alias="translationLanguages",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


