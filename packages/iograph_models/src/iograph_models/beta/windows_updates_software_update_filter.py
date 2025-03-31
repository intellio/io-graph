from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class WindowsUpdatesSoftwareUpdateFilter(BaseModel):
	odata_type: Literal["#microsoft.graph.windowsUpdates.softwareUpdateFilter"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.softwareUpdateFilter")

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
			if mapping_key == "#microsoft.graph.windowsUpdates.driverUpdateFilter":
				from .windows_updates_driver_update_filter import WindowsUpdatesDriverUpdateFilter
				return WindowsUpdatesDriverUpdateFilter.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUpdates.qualityUpdateFilter":
				from .windows_updates_quality_update_filter import WindowsUpdatesQualityUpdateFilter
				return WindowsUpdatesQualityUpdateFilter.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

