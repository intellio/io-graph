from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class MobileAppTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppTroubleshootingEvent"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppTroubleshootingEvent")
	additionalInformation: Optional[list[KeyValuePair]] = Field(alias="additionalInformation", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails", default=None,)
	applicationId: Optional[str] = Field(alias="applicationId", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	history: Optional[list[Annotated[Union[MobileAppTroubleshootingAppPolicyCreationHistory, MobileAppTroubleshootingAppStateHistory, MobileAppTroubleshootingAppTargetHistory, MobileAppTroubleshootingAppUpdateHistory, MobileAppTroubleshootingDeviceCheckinHistory],Field(discriminator="odata_type")]]] = Field(alias="history", default=None,)
	managedDeviceIdentifier: Optional[str] = Field(alias="managedDeviceIdentifier", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	appLogCollectionRequests: Optional[list[AppLogCollectionRequest]] = Field(alias="appLogCollectionRequests", default=None,)

from .key_value_pair import KeyValuePair
from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
from .mobile_app_troubleshooting_app_policy_creation_history import MobileAppTroubleshootingAppPolicyCreationHistory
from .mobile_app_troubleshooting_app_state_history import MobileAppTroubleshootingAppStateHistory
from .mobile_app_troubleshooting_app_target_history import MobileAppTroubleshootingAppTargetHistory
from .mobile_app_troubleshooting_app_update_history import MobileAppTroubleshootingAppUpdateHistory
from .mobile_app_troubleshooting_device_checkin_history import MobileAppTroubleshootingDeviceCheckinHistory
from .app_log_collection_request import AppLogCollectionRequest
