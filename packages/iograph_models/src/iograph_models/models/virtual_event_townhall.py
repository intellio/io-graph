from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class VirtualEventTownhall(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[CommunicationsIdentitySet] = Field(default=None,alias="createdBy",)
	description: Optional[ItemBody] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="endDateTime",)
	externalEventInformation: list[VirtualEventExternalInformation] = Field(alias="externalEventInformation",)
	settings: Optional[VirtualEventSettings] = Field(default=None,alias="settings",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)
	status: Optional[VirtualEventStatus] = Field(default=None,alias="status",)
	presenters: list[VirtualEventPresenter] = Field(alias="presenters",)
	sessions: list[VirtualEventSession] = Field(alias="sessions",)
	audience: Optional[MeetingAudience] = Field(default=None,alias="audience",)
	coOrganizers: list[CommunicationsUserIdentity] = Field(alias="coOrganizers",)
	invitedAttendees: list[Identity] = Field(alias="invitedAttendees",)
	isInviteOnly: Optional[bool] = Field(default=None,alias="isInviteOnly",)

from .communications_identity_set import CommunicationsIdentitySet
from .item_body import ItemBody
from .date_time_time_zone import DateTimeTimeZone
from .virtual_event_external_information import VirtualEventExternalInformation
from .virtual_event_settings import VirtualEventSettings
from .date_time_time_zone import DateTimeTimeZone
from .virtual_event_status import VirtualEventStatus
from .virtual_event_presenter import VirtualEventPresenter
from .virtual_event_session import VirtualEventSession
from .meeting_audience import MeetingAudience
from .communications_user_identity import CommunicationsUserIdentity
from .identity import Identity

