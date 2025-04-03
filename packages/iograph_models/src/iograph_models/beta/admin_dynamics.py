from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AdminDynamics(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.adminDynamics"] = Field(alias="@odata.type", default="#microsoft.graph.adminDynamics")
	customerVoice: Optional[CustomerVoiceSettings] = Field(alias="customerVoice", default=None,)

from .customer_voice_settings import CustomerVoiceSettings
