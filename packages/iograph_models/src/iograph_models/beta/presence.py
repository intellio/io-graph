from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Presence(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.presence"] = Field(alias="@odata.type", default="#microsoft.graph.presence")
	activity: Optional[str] = Field(alias="activity", default=None,)
	availability: Optional[str] = Field(alias="availability", default=None,)
	outOfOfficeSettings: Optional[OutOfOfficeSettings] = Field(alias="outOfOfficeSettings", default=None,)
	sequenceNumber: Optional[str] = Field(alias="sequenceNumber", default=None,)
	statusMessage: Optional[PresenceStatusMessage] = Field(alias="statusMessage", default=None,)

from .out_of_office_settings import OutOfOfficeSettings
from .presence_status_message import PresenceStatusMessage
