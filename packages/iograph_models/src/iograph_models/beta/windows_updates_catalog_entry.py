from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class WindowsUpdatesCatalogEntry(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	deployableUntilDateTime: Optional[datetime] = Field(alias="deployableUntilDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime", default=None,)

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
			if mapping_key == "#microsoft.graph.windowsUpdates.driverUpdateCatalogEntry":
				from .windows_updates_driver_update_catalog_entry import WindowsUpdatesDriverUpdateCatalogEntry
				return WindowsUpdatesDriverUpdateCatalogEntry.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.featureUpdateCatalogEntry":
				from .windows_updates_feature_update_catalog_entry import WindowsUpdatesFeatureUpdateCatalogEntry
				return WindowsUpdatesFeatureUpdateCatalogEntry.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.qualityUpdateCatalogEntry":
				from .windows_updates_quality_update_catalog_entry import WindowsUpdatesQualityUpdateCatalogEntry
				return WindowsUpdatesQualityUpdateCatalogEntry.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

