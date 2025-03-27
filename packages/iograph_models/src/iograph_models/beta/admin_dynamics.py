from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AdminDynamics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	customerVoice: Optional[CustomerVoiceSettings] = Field(alias="customerVoice", default=None,)

from .customer_voice_settings import CustomerVoiceSettings

