from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkMicrophoneConfiguration(BaseModel):
	isMicrophoneOptional: Optional[bool] = Field(alias="isMicrophoneOptional",default=None,)
	defaultMicrophone: Optional[TeamworkPeripheral] = Field(alias="defaultMicrophone",default=None,)
	microphones: Optional[list[TeamworkPeripheral]] = Field(alias="microphones",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_peripheral import TeamworkPeripheral
from .teamwork_peripheral import TeamworkPeripheral

