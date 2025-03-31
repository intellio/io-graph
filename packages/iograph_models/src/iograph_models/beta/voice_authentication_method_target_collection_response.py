from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VoiceAuthenticationMethodTargetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[VoiceAuthenticationMethodTarget]] = Field(alias="value", default=None,)

from .voice_authentication_method_target import VoiceAuthenticationMethodTarget
