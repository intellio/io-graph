from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class MobileAppTroubleshootingHistoryItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[MobileAppTroubleshootingAppPolicyCreationHistory, MobileAppTroubleshootingAppStateHistory, MobileAppTroubleshootingAppTargetHistory, MobileAppTroubleshootingAppUpdateHistory, MobileAppTroubleshootingDeviceCheckinHistory],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .mobile_app_troubleshooting_app_policy_creation_history import MobileAppTroubleshootingAppPolicyCreationHistory
from .mobile_app_troubleshooting_app_state_history import MobileAppTroubleshootingAppStateHistory
from .mobile_app_troubleshooting_app_target_history import MobileAppTroubleshootingAppTargetHistory
from .mobile_app_troubleshooting_app_update_history import MobileAppTroubleshootingAppUpdateHistory
from .mobile_app_troubleshooting_device_checkin_history import MobileAppTroubleshootingDeviceCheckinHistory
