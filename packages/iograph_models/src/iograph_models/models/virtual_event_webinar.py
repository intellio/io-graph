from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEventWebinar(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: Optional[CommunicationsIdentitySet] = Field(alias="createdBy",default=None,)
	description: Optional[ItemBody] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endDateTime: Optional[DateTimeTimeZone] = Field(alias="endDateTime",default=None,)
	externalEventInformation: Optional[list[VirtualEventExternalInformation]] = Field(alias="externalEventInformation",default=None,)
	settings: Optional[VirtualEventSettings] = Field(alias="settings",default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime",default=None,)
	status: Optional[str | VirtualEventStatus] = Field(alias="status",default=None,)
	presenters: Optional[list[VirtualEventPresenter]] = Field(alias="presenters",default=None,)
	sessions: Optional[list[VirtualEventSession]] = Field(alias="sessions",default=None,)
	audience: Optional[str | MeetingAudience] = Field(alias="audience",default=None,)
	coOrganizers: Optional[list[CommunicationsUserIdentity]] = Field(alias="coOrganizers",default=None,)
	registrationConfiguration: Optional[VirtualEventWebinarRegistrationConfiguration] = Field(alias="registrationConfiguration",default=None,)
	registrations: Optional[list[VirtualEventRegistration]] = Field(alias="registrations",default=None,)

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
from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
from .virtual_event_registration import VirtualEventRegistration

