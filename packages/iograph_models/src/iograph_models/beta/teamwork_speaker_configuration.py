from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkSpeakerConfiguration(BaseModel):
	isCommunicationSpeakerOptional: Optional[bool] = Field(alias="isCommunicationSpeakerOptional", default=None,)
	isSpeakerOptional: Optional[bool] = Field(alias="isSpeakerOptional", default=None,)
	defaultCommunicationSpeaker: Optional[TeamworkPeripheral] = Field(alias="defaultCommunicationSpeaker", default=None,)
	defaultSpeaker: Optional[TeamworkPeripheral] = Field(alias="defaultSpeaker", default=None,)
	speakers: Optional[list[TeamworkPeripheral]] = Field(alias="speakers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral

