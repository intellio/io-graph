from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdBy: Optional[CommunicationsIdentitySet] = Field(alias="createdBy", default=None,)
	description: Optional[ItemBody] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDateTime: Optional[DateTimeTimeZone] = Field(alias="endDateTime", default=None,)
	externalEventInformation: Optional[list[VirtualEventExternalInformation]] = Field(alias="externalEventInformation", default=None,)
	settings: Optional[VirtualEventSettings] = Field(alias="settings", default=None,)
	startDateTime: Optional[DateTimeTimeZone] = Field(alias="startDateTime", default=None,)
	status: Optional[VirtualEventStatus | str] = Field(alias="status", default=None,)
	presenters: Optional[list[VirtualEventPresenter]] = Field(alias="presenters", default=None,)
	sessions: Optional[list[VirtualEventSession]] = Field(alias="sessions", default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.virtualEventTownhall":
				from .virtual_event_townhall import VirtualEventTownhall
				return VirtualEventTownhall.model_validate(data)
			if mapping_key == "#microsoft.graph.virtualEventWebinar":
				from .virtual_event_webinar import VirtualEventWebinar
				return VirtualEventWebinar.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .communications_identity_set import CommunicationsIdentitySet
from .item_body import ItemBody
from .date_time_time_zone import DateTimeTimeZone
from .virtual_event_external_information import VirtualEventExternalInformation
from .virtual_event_settings import VirtualEventSettings
from .date_time_time_zone import DateTimeTimeZone
from .virtual_event_status import VirtualEventStatus
from .virtual_event_presenter import VirtualEventPresenter
from .virtual_event_session import VirtualEventSession

