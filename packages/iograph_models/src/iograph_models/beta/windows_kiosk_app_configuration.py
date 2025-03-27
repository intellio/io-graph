from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskAppConfiguration(BaseModel):
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
			if mapping_key == "#microsoft.graph.windowsKioskMultipleApps":
				from .windows_kiosk_multiple_apps import WindowsKioskMultipleApps
				return WindowsKioskMultipleApps.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskSingleUWPApp":
				from .windows_kiosk_single_u_w_p_app import WindowsKioskSingleUWPApp
				return WindowsKioskSingleUWPApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskSingleWin32App":
				from .windows_kiosk_single_win32_app import WindowsKioskSingleWin32App
				return WindowsKioskSingleWin32App.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


