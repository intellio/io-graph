from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class IosWebContentFilterBase(BaseModel):
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
			if mapping_key == "#microsoft.graph.iosWebContentFilterAutoFilter":
				from .ios_web_content_filter_auto_filter import IosWebContentFilterAutoFilter
				return IosWebContentFilterAutoFilter.model_validate(data)
			if mapping_key == "#microsoft.graph.iosWebContentFilterSpecificWebsitesAccess":
				from .ios_web_content_filter_specific_websites_access import IosWebContentFilterSpecificWebsitesAccess
				return IosWebContentFilterSpecificWebsitesAccess.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


