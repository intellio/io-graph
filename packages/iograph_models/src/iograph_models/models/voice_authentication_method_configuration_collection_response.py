from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VoiceAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[VoiceAuthenticationMethodConfiguration] = Field(alias="value",)

from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration

