from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any


class CloudPcBulkAction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	actionSummary: Optional[CloudPcBulkActionSummary] = Field(alias="actionSummary", default=None,)
	cloudPcIds: Optional[list[str]] = Field(alias="cloudPcIds", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	initiatedByUserPrincipalName: Optional[str] = Field(alias="initiatedByUserPrincipalName", default=None,)
	scheduledDuringMaintenanceWindow: Optional[bool] = Field(alias="scheduledDuringMaintenanceWindow", default=None,)
	status: Optional[CloudPcBulkActionStatus | str] = Field(alias="status", default=None,)

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
			if mapping_key == "#microsoft.graph.cloudPcBulkCreateSnapshot":
				from .cloud_pc_bulk_create_snapshot import CloudPcBulkCreateSnapshot
				return CloudPcBulkCreateSnapshot.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailback":
				from .cloud_pc_bulk_disaster_recovery_failback import CloudPcBulkDisasterRecoveryFailback
				return CloudPcBulkDisasterRecoveryFailback.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkDisasterRecoveryFailover":
				from .cloud_pc_bulk_disaster_recovery_failover import CloudPcBulkDisasterRecoveryFailover
				return CloudPcBulkDisasterRecoveryFailover.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkModifyDiskEncryptionType":
				from .cloud_pc_bulk_modify_disk_encryption_type import CloudPcBulkModifyDiskEncryptionType
				return CloudPcBulkModifyDiskEncryptionType.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkMove":
				from .cloud_pc_bulk_move import CloudPcBulkMove
				return CloudPcBulkMove.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkPowerOff":
				from .cloud_pc_bulk_power_off import CloudPcBulkPowerOff
				return CloudPcBulkPowerOff.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkPowerOn":
				from .cloud_pc_bulk_power_on import CloudPcBulkPowerOn
				return CloudPcBulkPowerOn.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkReprovision":
				from .cloud_pc_bulk_reprovision import CloudPcBulkReprovision
				return CloudPcBulkReprovision.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkResize":
				from .cloud_pc_bulk_resize import CloudPcBulkResize
				return CloudPcBulkResize.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkRestart":
				from .cloud_pc_bulk_restart import CloudPcBulkRestart
				return CloudPcBulkRestart.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkRestore":
				from .cloud_pc_bulk_restore import CloudPcBulkRestore
				return CloudPcBulkRestore.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkSetReviewStatus":
				from .cloud_pc_bulk_set_review_status import CloudPcBulkSetReviewStatus
				return CloudPcBulkSetReviewStatus.model_validate(data)
			if mapping_key == "#microsoft.graph.cloudPcBulkTroubleshoot":
				from .cloud_pc_bulk_troubleshoot import CloudPcBulkTroubleshoot
				return CloudPcBulkTroubleshoot.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .cloud_pc_bulk_action_summary import CloudPcBulkActionSummary
from .cloud_pc_bulk_action_status import CloudPcBulkActionStatus
