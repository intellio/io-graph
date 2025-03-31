from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DlpEvaluationInput(BaseModel):
	currentLabel: Optional[CurrentLabel] = Field(alias="currentLabel", default=None,)
	discoveredSensitiveTypes: Optional[list[DiscoveredSensitiveType]] = Field(alias="discoveredSensitiveTypes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

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
			if mapping_key == "#microsoft.graph.dlpEvaluationWindowsDevicesInput":
				from .dlp_evaluation_windows_devices_input import DlpEvaluationWindowsDevicesInput
				return DlpEvaluationWindowsDevicesInput.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .current_label import CurrentLabel
from .discovered_sensitive_type import DiscoveredSensitiveType
