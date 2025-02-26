from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from datetime import datetime
from pydantic import BaseModel, Field


class DeviceActionResult(BaseModel):
	actionName: Optional[str] = Field(default=None,alias="actionName",)
	actionState: Optional[ActionState] = Field(default=None,alias="actionState",)
	lastUpdatedDateTime: Optional[datetime] = Field(default=None,alias="lastUpdatedDateTime",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

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
			if mapping_key == "#microsoft.graph.deleteUserFromSharedAppleDeviceActionResult":
				from .delete_user_from_shared_apple_device_action_result import DeleteUserFromSharedAppleDeviceActionResult
				return DeleteUserFromSharedAppleDeviceActionResult.model_validate(data)
			if mapping_key == "#microsoft.graph.locateDeviceActionResult":
				from .locate_device_action_result import LocateDeviceActionResult
				return LocateDeviceActionResult.model_validate(data)
			if mapping_key == "#microsoft.graph.remoteLockActionResult":
				from .remote_lock_action_result import RemoteLockActionResult
				return RemoteLockActionResult.model_validate(data)
			if mapping_key == "#microsoft.graph.resetPasscodeActionResult":
				from .reset_passcode_action_result import ResetPasscodeActionResult
				return ResetPasscodeActionResult.model_validate(data)
			if mapping_key == "#microsoft.graph.rotateBitLockerKeysDeviceActionResult":
				from .rotate_bit_locker_keys_device_action_result import RotateBitLockerKeysDeviceActionResult
				return RotateBitLockerKeysDeviceActionResult.model_validate(data)
			if mapping_key == "#microsoft.graph.windowsDefenderScanActionResult":
				from .windows_defender_scan_action_result import WindowsDefenderScanActionResult
				return WindowsDefenderScanActionResult.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e

from .action_state import ActionState

