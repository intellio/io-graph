from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppTroubleshootingDeviceCheckinHistory(BaseModel):
	occurrenceDateTime: Optional[datetime] = Field(alias="occurrenceDateTime",default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails

