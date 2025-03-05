from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsInformationProtectionApp(BaseModel):
	denied: Optional[bool] = Field(alias="denied",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	productName: Optional[str] = Field(alias="productName",default=None,)
	publisherName: Optional[str] = Field(alias="publisherName",default=None,)
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
			if mapping_key == "#microsoft.graph.windowsInformationProtectionDesktopApp":
				from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
				return WindowsInformationProtectionDesktopApp.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsInformationProtectionStoreApp":
				from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp
				return WindowsInformationProtectionStoreApp.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


