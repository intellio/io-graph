from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class EdgeHomeButtonConfiguration(BaseModel):
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
			if mapping_key == "#microsoft.graph.edgeHomeButtonHidden":
				from .edge_home_button_hidden import EdgeHomeButtonHidden
				return EdgeHomeButtonHidden.model_validate(data)
			if mapping_key == "#microsoft.graph.edgeHomeButtonLoadsStartPage":
				from .edge_home_button_loads_start_page import EdgeHomeButtonLoadsStartPage
				return EdgeHomeButtonLoadsStartPage.model_validate(data)
			if mapping_key == "#microsoft.graph.edgeHomeButtonOpensCustomURL":
				from .edge_home_button_opens_custom_u_r_l import EdgeHomeButtonOpensCustomURL
				return EdgeHomeButtonOpensCustomURL.model_validate(data)
			if mapping_key == "#microsoft.graph.edgeHomeButtonOpensNewTab":
				from .edge_home_button_opens_new_tab import EdgeHomeButtonOpensNewTab
				return EdgeHomeButtonOpensNewTab.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


