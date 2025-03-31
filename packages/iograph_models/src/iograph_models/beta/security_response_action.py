from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class SecurityResponseAction(BaseModel):
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
			if mapping_key == "#microsoft.graph.security.allowFileResponseAction":
				from .security_allow_file_response_action import SecurityAllowFileResponseAction
				return SecurityAllowFileResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.blockFileResponseAction":
				from .security_block_file_response_action import SecurityBlockFileResponseAction
				return SecurityBlockFileResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.collectInvestigationPackageResponseAction":
				from .security_collect_investigation_package_response_action import SecurityCollectInvestigationPackageResponseAction
				return SecurityCollectInvestigationPackageResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.disableUserResponseAction":
				from .security_disable_user_response_action import SecurityDisableUserResponseAction
				return SecurityDisableUserResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.forceUserPasswordResetResponseAction":
				from .security_force_user_password_reset_response_action import SecurityForceUserPasswordResetResponseAction
				return SecurityForceUserPasswordResetResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.hardDeleteResponseAction":
				from .security_hard_delete_response_action import SecurityHardDeleteResponseAction
				return SecurityHardDeleteResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.initiateInvestigationResponseAction":
				from .security_initiate_investigation_response_action import SecurityInitiateInvestigationResponseAction
				return SecurityInitiateInvestigationResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.isolateDeviceResponseAction":
				from .security_isolate_device_response_action import SecurityIsolateDeviceResponseAction
				return SecurityIsolateDeviceResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.markUserAsCompromisedResponseAction":
				from .security_mark_user_as_compromised_response_action import SecurityMarkUserAsCompromisedResponseAction
				return SecurityMarkUserAsCompromisedResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.moveToDeletedItemsResponseAction":
				from .security_move_to_deleted_items_response_action import SecurityMoveToDeletedItemsResponseAction
				return SecurityMoveToDeletedItemsResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.moveToInboxResponseAction":
				from .security_move_to_inbox_response_action import SecurityMoveToInboxResponseAction
				return SecurityMoveToInboxResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.moveToJunkResponseAction":
				from .security_move_to_junk_response_action import SecurityMoveToJunkResponseAction
				return SecurityMoveToJunkResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.restrictAppExecutionResponseAction":
				from .security_restrict_app_execution_response_action import SecurityRestrictAppExecutionResponseAction
				return SecurityRestrictAppExecutionResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.runAntivirusScanResponseAction":
				from .security_run_antivirus_scan_response_action import SecurityRunAntivirusScanResponseAction
				return SecurityRunAntivirusScanResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.softDeleteResponseAction":
				from .security_soft_delete_response_action import SecuritySoftDeleteResponseAction
				return SecuritySoftDeleteResponseAction.model_validate(data)
			if mapping_key == "#microsoft.graph.security.stopAndQuarantineFileResponseAction":
				from .security_stop_and_quarantine_file_response_action import SecurityStopAndQuarantineFileResponseAction
				return SecurityStopAndQuarantineFileResponseAction.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

