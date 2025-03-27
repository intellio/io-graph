from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ChangeItemBase(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	changeItemService: Optional[str] = Field(alias="changeItemService", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	documentationUrls: Optional[list[str]] = Field(alias="documentationUrls", default=None,)
	shortDescription: Optional[str] = Field(alias="shortDescription", default=None,)
	systemTags: Optional[list[str]] = Field(alias="systemTags", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)

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
			if mapping_key == "#microsoft.graph.announcement":
				from .announcement import Announcement
				return Announcement.model_validate(data)
			if mapping_key == "#microsoft.graph.roadmap":
				from .roadmap import Roadmap
				return Roadmap.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


