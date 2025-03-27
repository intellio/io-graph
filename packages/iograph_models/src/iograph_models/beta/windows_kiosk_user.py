from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsKioskUser(BaseModel):
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
			if mapping_key == "#microsoft.graph.windowsKioskActiveDirectoryGroup":
				from .windows_kiosk_active_directory_group import WindowsKioskActiveDirectoryGroup
				return WindowsKioskActiveDirectoryGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskAutologon":
				from .windows_kiosk_autologon import WindowsKioskAutologon
				return WindowsKioskAutologon.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskAzureADGroup":
				from .windows_kiosk_azure_a_d_group import WindowsKioskAzureADGroup
				return WindowsKioskAzureADGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskAzureADUser":
				from .windows_kiosk_azure_a_d_user import WindowsKioskAzureADUser
				return WindowsKioskAzureADUser.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskLocalGroup":
				from .windows_kiosk_local_group import WindowsKioskLocalGroup
				return WindowsKioskLocalGroup.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskLocalUser":
				from .windows_kiosk_local_user import WindowsKioskLocalUser
				return WindowsKioskLocalUser.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsKioskVisitor":
				from .windows_kiosk_visitor import WindowsKioskVisitor
				return WindowsKioskVisitor.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


