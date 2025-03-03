from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field


class OfficeGraphInsights(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	shared: Optional[list[SharedInsight]] = Field(default=None,alias="shared",)
	trending: Optional[list[Trending]] = Field(default=None,alias="trending",)
	used: Optional[list[UsedInsight]] = Field(default=None,alias="used",)

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
			if mapping_key == "#microsoft.graph.itemInsights":
				from .item_insights import ItemInsights
				return ItemInsights.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .shared_insight import SharedInsight
from .trending import Trending
from .used_insight import UsedInsight

