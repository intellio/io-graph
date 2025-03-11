from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	additionalInformation: Optional[list[KeyValuePair]] = Field(alias="additionalInformation",default=None,)
	correlationId: Optional[str] = Field(alias="correlationId",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	eventName: Optional[str] = Field(alias="eventName",default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails",default=None,)
	applicationId: Optional[str] = Field(alias="applicationId",default=None,)
	deviceId: Optional[str] = Field(alias="deviceId",default=None,)
	history: SerializeAsAny[Optional[list[MobileAppTroubleshootingHistoryItem]]] = Field(alias="history",default=None,)
	managedDeviceIdentifier: Optional[str] = Field(alias="managedDeviceIdentifier",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	appLogCollectionRequests: Optional[list[AppLogCollectionRequest]] = Field(alias="appLogCollectionRequests",default=None,)

from .key_value_pair import KeyValuePair
from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
from .mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem
from .app_log_collection_request import AppLogCollectionRequest

