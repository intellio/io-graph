from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VoiceAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[VoiceAuthenticationMethodConfiguration]] = Field(alias="value",default=None,)

from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration

