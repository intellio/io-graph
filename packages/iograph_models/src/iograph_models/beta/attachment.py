from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class Attachment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	contentType: Optional[str] = Field(alias="contentType", default=None,)
	isInline: Optional[bool] = Field(alias="isInline", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)

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
			if mapping_key == "#microsoft.graph.fileAttachment":
				from .file_attachment import FileAttachment
				return FileAttachment.model_validate(data)
			if mapping_key == "#microsoft.graph.itemAttachment":
				from .item_attachment import ItemAttachment
				return ItemAttachment.model_validate(data)
			if mapping_key == "#microsoft.graph.referenceAttachment":
				from .reference_attachment import ReferenceAttachment
				return ReferenceAttachment.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

