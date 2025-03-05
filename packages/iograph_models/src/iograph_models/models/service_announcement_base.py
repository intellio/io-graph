from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceAnnouncementBase(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	details: Optional[list[KeyValuePair]] = Field(default=None,alias="details",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	title: Optional[str] = Field(default=None,alias="title",)

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
			if mapping_key == "#microsoft.graph.serviceHealthIssue":
				from .service_health_issue import ServiceHealthIssue
				return ServiceHealthIssue.model_validate(data)
			if mapping_key == "#microsoft.graph.serviceUpdateMessage":
				from .service_update_message import ServiceUpdateMessage
				return ServiceUpdateMessage.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .key_value_pair import KeyValuePair

