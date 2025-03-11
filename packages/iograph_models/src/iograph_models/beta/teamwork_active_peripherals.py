from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkActivePeripherals(BaseModel):
	communicationSpeaker: Optional[TeamworkPeripheral] = Field(alias="communicationSpeaker",default=None,)
	contentCamera: Optional[TeamworkPeripheral] = Field(alias="contentCamera",default=None,)
	microphone: Optional[TeamworkPeripheral] = Field(alias="microphone",default=None,)
	roomCamera: Optional[TeamworkPeripheral] = Field(alias="roomCamera",default=None,)
	speaker: Optional[TeamworkPeripheral] = Field(alias="speaker",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral

