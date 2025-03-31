from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class DepEnrollmentBaseProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.depEnrollmentBaseProfile"] = Field(alias="@odata.type", default="#microsoft.graph.depEnrollmentBaseProfile")
	configurationEndpointUrl: Optional[str] = Field(alias="configurationEndpointUrl", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enableAuthenticationViaCompanyPortal: Optional[bool] = Field(alias="enableAuthenticationViaCompanyPortal", default=None,)
	requireCompanyPortalOnSetupAssistantEnrolledDevices: Optional[bool] = Field(alias="requireCompanyPortalOnSetupAssistantEnrolledDevices", default=None,)
	requiresUserAuthentication: Optional[bool] = Field(alias="requiresUserAuthentication", default=None,)
	appleIdDisabled: Optional[bool] = Field(alias="appleIdDisabled", default=None,)
	applePayDisabled: Optional[bool] = Field(alias="applePayDisabled", default=None,)
	configurationWebUrl: Optional[bool] = Field(alias="configurationWebUrl", default=None,)
	deviceNameTemplate: Optional[str] = Field(alias="deviceNameTemplate", default=None,)
	diagnosticsDisabled: Optional[bool] = Field(alias="diagnosticsDisabled", default=None,)
	displayToneSetupDisabled: Optional[bool] = Field(alias="displayToneSetupDisabled", default=None,)
	enabledSkipKeys: Optional[list[str]] = Field(alias="enabledSkipKeys", default=None,)
	enrollmentTimeAzureAdGroupIds: Optional[list[UUID]] = Field(alias="enrollmentTimeAzureAdGroupIds", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	isMandatory: Optional[bool] = Field(alias="isMandatory", default=None,)
	locationDisabled: Optional[bool] = Field(alias="locationDisabled", default=None,)
	privacyPaneDisabled: Optional[bool] = Field(alias="privacyPaneDisabled", default=None,)
	profileRemovalDisabled: Optional[bool] = Field(alias="profileRemovalDisabled", default=None,)
	restoreBlocked: Optional[bool] = Field(alias="restoreBlocked", default=None,)
	screenTimeScreenDisabled: Optional[bool] = Field(alias="screenTimeScreenDisabled", default=None,)
	siriDisabled: Optional[bool] = Field(alias="siriDisabled", default=None,)
	supervisedModeEnabled: Optional[bool] = Field(alias="supervisedModeEnabled", default=None,)
	supportDepartment: Optional[str] = Field(alias="supportDepartment", default=None,)
	supportPhoneNumber: Optional[str] = Field(alias="supportPhoneNumber", default=None,)
	termsAndConditionsDisabled: Optional[bool] = Field(alias="termsAndConditionsDisabled", default=None,)
	touchIdDisabled: Optional[bool] = Field(alias="touchIdDisabled", default=None,)
	waitForDeviceConfiguredConfirmation: Optional[bool] = Field(alias="waitForDeviceConfiguredConfirmation", default=None,)

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
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

