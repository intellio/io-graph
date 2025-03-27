from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class MarkContent(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.markContent"] = Field(alias="@odata.type", default="#microsoft.graph.markContent")
	fontColor: Optional[str] = Field(alias="fontColor", default=None,)
	fontSize: Optional[int] = Field(alias="fontSize", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)

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
			if mapping_key == "#microsoft.graph.addFooter":
				from .add_footer import AddFooter
				return AddFooter.model_validate(data)
			if mapping_key == "#microsoft.graph.addHeader":
				from .add_header import AddHeader
				return AddHeader.model_validate(data)
			if mapping_key == "#microsoft.graph.addWatermark":
				from .add_watermark import AddWatermark
				return AddWatermark.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


