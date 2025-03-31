from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class EnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	configurationEndpointUrl: Optional[str] = Field(alias="configurationEndpointUrl", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enableAuthenticationViaCompanyPortal: Optional[bool] = Field(alias="enableAuthenticationViaCompanyPortal", default=None,)
	requireCompanyPortalOnSetupAssistantEnrolledDevices: Optional[bool] = Field(alias="requireCompanyPortalOnSetupAssistantEnrolledDevices", default=None,)
	requiresUserAuthentication: Optional[bool] = Field(alias="requiresUserAuthentication", default=None,)

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
			if mapping_key == "#microsoft.graph.depIOSEnrollmentProfile":
				from .dep_i_o_s_enrollment_profile import DepIOSEnrollmentProfile
				return DepIOSEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depMacOSEnrollmentProfile":
				from .dep_mac_o_s_enrollment_profile import DepMacOSEnrollmentProfile
				return DepMacOSEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depEnrollmentProfile":
				from .dep_enrollment_profile import DepEnrollmentProfile
				return DepEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depTvOSEnrollmentProfile":
				from .dep_tv_o_s_enrollment_profile import DepTvOSEnrollmentProfile
				return DepTvOSEnrollmentProfile.model_validate(data)
			if mapping_key == "#microsoft.graph.depVisionOSEnrollmentProfile":
				from .dep_vision_o_s_enrollment_profile import DepVisionOSEnrollmentProfile
				return DepVisionOSEnrollmentProfile.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

