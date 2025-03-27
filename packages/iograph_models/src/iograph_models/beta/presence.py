from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Presence(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activity: Optional[str] = Field(alias="activity", default=None,)
	availability: Optional[str] = Field(alias="availability", default=None,)
	outOfOfficeSettings: Optional[OutOfOfficeSettings] = Field(alias="outOfOfficeSettings", default=None,)
	sequenceNumber: Optional[str] = Field(alias="sequenceNumber", default=None,)
	statusMessage: Optional[PresenceStatusMessage] = Field(alias="statusMessage", default=None,)

from .out_of_office_settings import OutOfOfficeSettings
from .presence_status_message import PresenceStatusMessage

