from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MobileAppTroubleshootingDeviceCheckinHistory(BaseModel):
	occurrenceDateTime: Optional[datetime] = Field(alias="occurrenceDateTime", default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppTroubleshootingDeviceCheckinHistory"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppTroubleshootingDeviceCheckinHistory")

from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
