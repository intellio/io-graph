from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MeetingParticipants(BaseModel):
	attendees: Optional[list[Annotated[Union[VirtualEventPresenterInfo],Field(discriminator="odata_type")]]] = Field(alias="attendees", default=None,)
	organizer: Optional[Union[VirtualEventPresenterInfo]] = Field(alias="organizer", default=None,discriminator="odata_type", )
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .virtual_event_presenter_info import VirtualEventPresenterInfo
from .virtual_event_presenter_info import VirtualEventPresenterInfo

