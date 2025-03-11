from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ParentLabelDetails(BaseModel):
	color: Optional[str] = Field(alias="color",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	isActive: Optional[bool] = Field(alias="isActive",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	parent: SerializeAsAny[Optional[ParentLabelDetails]] = Field(alias="parent",default=None,)
	sensitivity: Optional[int] = Field(alias="sensitivity",default=None,)
	tooltip: Optional[str] = Field(alias="tooltip",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

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
			if mapping_key == "#microsoft.graph.labelDetails":
				from .label_details import LabelDetails
				return LabelDetails.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


