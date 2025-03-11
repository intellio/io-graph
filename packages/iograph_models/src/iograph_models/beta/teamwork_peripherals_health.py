from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkPeripheralsHealth(BaseModel):
	communicationSpeakerHealth: Optional[TeamworkPeripheralHealth] = Field(alias="communicationSpeakerHealth",default=None,)
	contentCameraHealth: Optional[TeamworkPeripheralHealth] = Field(alias="contentCameraHealth",default=None,)
	displayHealthCollection: Optional[list[TeamworkPeripheralHealth]] = Field(alias="displayHealthCollection",default=None,)
	microphoneHealth: Optional[TeamworkPeripheralHealth] = Field(alias="microphoneHealth",default=None,)
	roomCameraHealth: Optional[TeamworkPeripheralHealth] = Field(alias="roomCameraHealth",default=None,)
	speakerHealth: Optional[TeamworkPeripheralHealth] = Field(alias="speakerHealth",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_peripheral_health import TeamworkPeripheralHealth
from .teamwork_peripheral_health import TeamworkPeripheralHealth
from .teamwork_peripheral_health import TeamworkPeripheralHealth
from .teamwork_peripheral_health import TeamworkPeripheralHealth
from .teamwork_peripheral_health import TeamworkPeripheralHealth
from .teamwork_peripheral_health import TeamworkPeripheralHealth

