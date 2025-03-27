from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalMeetingRegistration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalMeetingRegistration"] = Field(alias="@odata.type", default="#microsoft.graph.externalMeetingRegistration")
	allowedRegistrant: Optional[MeetingAudience | str] = Field(alias="allowedRegistrant", default=None,)
	registrants: Optional[list[Annotated[Union[ExternalMeetingRegistrant, MeetingRegistrant]],Field(discriminator="odata_type")]]] = Field(alias="registrants", default=None,)

from .meeting_audience import MeetingAudience
from .external_meeting_registrant import ExternalMeetingRegistrant
from .meeting_registrant import MeetingRegistrant

