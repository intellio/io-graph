from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppAssignmentSettings(BaseModel):
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
			if mapping_key == "#microsoft.graph.iosLobAppAssignmentSettings":
				from .ios_lob_app_assignment_settings import IosLobAppAssignmentSettings
				return IosLobAppAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.iosStoreAppAssignmentSettings":
				from .ios_store_app_assignment_settings import IosStoreAppAssignmentSettings
				return IosStoreAppAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppAppAssignmentSettings":
				from .ios_vpp_app_assignment_settings import IosVppAppAssignmentSettings
				return IosVppAppAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.macOsLobAppAssignmentSettings":
				from .mac_os_lob_app_assignment_settings import MacOsLobAppAssignmentSettings
				return MacOsLobAppAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.microsoftStoreForBusinessAppAssignmentSettings":
				from .microsoft_store_for_business_app_assignment_settings import MicrosoftStoreForBusinessAppAssignmentSettings
				return MicrosoftStoreForBusinessAppAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.win32LobAppAssignmentSettings":
				from .win32_lob_app_assignment_settings import Win32LobAppAssignmentSettings
				return Win32LobAppAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsAppXAppAssignmentSettings":
				from .windows_app_x_app_assignment_settings import WindowsAppXAppAssignmentSettings
				return WindowsAppXAppAssignmentSettings.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsUniversalAppXAppAssignmentSettings":
				from .windows_universal_app_x_app_assignment_settings import WindowsUniversalAppXAppAssignmentSettings
				return WindowsUniversalAppXAppAssignmentSettings.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


