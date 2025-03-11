from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsUrlToItemResolverBase(BaseModel):
	priority: Optional[int] = Field(alias="priority",default=None,)
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
			if mapping_key == "#microsoft.graph.externalConnectors.itemIdResolver":
				from .external_connectors_item_id_resolver import ExternalConnectorsItemIdResolver
				return ExternalConnectorsItemIdResolver.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


