from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class OutlookItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	categories: Optional[list[str]] = Field(alias="categories", default=None,)
	changeKey: Optional[str] = Field(alias="changeKey", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)

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
			if mapping_key == "#microsoft.graph.contact":
				from .contact import Contact
				return Contact.model_validate(data)
			if mapping_key == "#microsoft.graph.event":
				from .event import Event
				return Event.model_validate(data)
			if mapping_key == "#microsoft.graph.mailboxItem":
				from .mailbox_item import MailboxItem
				return MailboxItem.model_validate(data)
			if mapping_key == "#microsoft.graph.calendarSharingMessage":
				from .calendar_sharing_message import CalendarSharingMessage
				return CalendarSharingMessage.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessageRequest":
				from .event_message_request import EventMessageRequest
				return EventMessageRequest.model_validate(data)
			if mapping_key == "#microsoft.graph.eventMessageResponse":
				from .event_message_response import EventMessageResponse
				return EventMessageResponse.model_validate(data)
			if mapping_key == "#microsoft.graph.note":
				from .note import Note
				return Note.model_validate(data)
			if mapping_key == "#microsoft.graph.outlookTask":
				from .outlook_task import OutlookTask
				return OutlookTask.model_validate(data)
			if mapping_key == "#microsoft.graph.post":
				from .post import Post
				return Post.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

