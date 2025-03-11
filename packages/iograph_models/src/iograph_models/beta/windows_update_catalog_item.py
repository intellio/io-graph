from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateCatalogItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endOfSupportDate: Optional[datetime] = Field(alias="endOfSupportDate",default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime",default=None,)

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
			if mapping_key == "#microsoft.graph.windowsFeatureUpdateCatalogItem":
				from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
				return WindowsFeatureUpdateCatalogItem.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsQualityUpdateCatalogItem":
				from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem
				return WindowsQualityUpdateCatalogItem.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


