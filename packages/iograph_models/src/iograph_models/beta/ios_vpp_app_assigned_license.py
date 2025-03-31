from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class IosVppAppAssignedLicense(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	userEmailAddress: Optional[str] = Field(alias="userEmailAddress", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userName: Optional[str] = Field(alias="userName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

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
			if mapping_key == "#microsoft.graph.iosVppAppAssignedDeviceLicense":
				from .ios_vpp_app_assigned_device_license import IosVppAppAssignedDeviceLicense
				return IosVppAppAssignedDeviceLicense.model_validate(data)
			if mapping_key == "#microsoft.graph.iosVppAppAssignedUserLicense":
				from .ios_vpp_app_assigned_user_license import IosVppAppAssignedUserLicense
				return IosVppAppAssignedUserLicense.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

