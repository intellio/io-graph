from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppTroubleshootingHistoryItem(BaseModel):
	occurrenceDateTime: Optional[datetime] = Field(alias="occurrenceDateTime", default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails", default=None,)
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
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingAppPolicyCreationHistory":
				from .mobile_app_troubleshooting_app_policy_creation_history import MobileAppTroubleshootingAppPolicyCreationHistory
				return MobileAppTroubleshootingAppPolicyCreationHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingAppStateHistory":
				from .mobile_app_troubleshooting_app_state_history import MobileAppTroubleshootingAppStateHistory
				return MobileAppTroubleshootingAppStateHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingAppTargetHistory":
				from .mobile_app_troubleshooting_app_target_history import MobileAppTroubleshootingAppTargetHistory
				return MobileAppTroubleshootingAppTargetHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingAppUpdateHistory":
				from .mobile_app_troubleshooting_app_update_history import MobileAppTroubleshootingAppUpdateHistory
				return MobileAppTroubleshootingAppUpdateHistory.model_validate(data)
			if mapping_key == "#microsoft.graph.mobileAppTroubleshootingDeviceCheckinHistory":
				from .mobile_app_troubleshooting_device_checkin_history import MobileAppTroubleshootingDeviceCheckinHistory
				return MobileAppTroubleshootingDeviceCheckinHistory.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails

