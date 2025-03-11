from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WorkplaceSensorEventValue(BaseModel):
	eventType: Optional[WorkplaceSensorEventType | str] = Field(alias="eventType",default=None,)
	user: Optional[EmailIdentity] = Field(alias="user",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .workplace_sensor_event_type import WorkplaceSensorEventType
from .email_identity import EmailIdentity

