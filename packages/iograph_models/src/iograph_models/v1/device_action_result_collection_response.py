from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DeviceActionResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeleteUserFromSharedAppleDeviceActionResult, LocateDeviceActionResult, RemoteLockActionResult, ResetPasscodeActionResult, RotateBitLockerKeysDeviceActionResult, WindowsDefenderScanActionResult],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .delete_user_from_shared_apple_device_action_result import DeleteUserFromSharedAppleDeviceActionResult
from .locate_device_action_result import LocateDeviceActionResult
from .remote_lock_action_result import RemoteLockActionResult
from .reset_passcode_action_result import ResetPasscodeActionResult
from .rotate_bit_locker_keys_device_action_result import RotateBitLockerKeysDeviceActionResult
from .windows_defender_scan_action_result import WindowsDefenderScanActionResult
