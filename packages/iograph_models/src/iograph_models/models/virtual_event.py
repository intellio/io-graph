from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class VirtualEvent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[CommunicationsIdentitySet] = Field(default=None,alias="createdBy",)
	description: Optional[ItemBody] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="endDateTime",)
	externalEventInformation: Optional[list[VirtualEventExternalInformation]] = Field(default=None,alias="externalEventInformation",)
	settings: Optional[VirtualEventSettings] = Field(default=None,alias="settings",)
	startDateTime: Optional[DateTimeTimeZone] = Field(default=None,alias="startDateTime",)
	status: Optional[VirtualEventStatus] = Field(default=None,alias="status",)
	presenters: Optional[list[VirtualEventPresenter]] = Field(default=None,alias="presenters",)
	sessions: Optional[list[VirtualEventSession]] = Field(default=None,alias="sessions",)

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

