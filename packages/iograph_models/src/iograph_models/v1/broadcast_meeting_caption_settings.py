from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BroadcastMeetingCaptionSettings(BaseModel):
	isCaptionEnabled: Optional[bool] = Field(alias="isCaptionEnabled",default=None,)
	spokenLanguage: Optional[str] = Field(alias="spokenLanguage",default=None,)
	translationLanguages: Optional[list[str]] = Field(alias="translationLanguages",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


