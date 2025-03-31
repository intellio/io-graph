from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class MobileAppCatalogPackage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	productDisplayName: Optional[str] = Field(alias="productDisplayName", default=None,)
	productId: Optional[str] = Field(alias="productId", default=None,)
	publisherDisplayName: Optional[str] = Field(alias="publisherDisplayName", default=None,)
	versionDisplayName: Optional[str] = Field(alias="versionDisplayName", default=None,)

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
			if mapping_key == "#microsoft.graph.win32MobileAppCatalogPackage":
				from .win32_mobile_app_catalog_package import Win32MobileAppCatalogPackage
				return Win32MobileAppCatalogPackage.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

