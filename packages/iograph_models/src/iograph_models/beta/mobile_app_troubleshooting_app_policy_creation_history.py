from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MobileAppTroubleshootingAppPolicyCreationHistory(BaseModel):
	occurrenceDateTime: Optional[datetime] = Field(alias="occurrenceDateTime", default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppTroubleshootingAppPolicyCreationHistory"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppTroubleshootingAppPolicyCreationHistory")
	errorCode: Optional[str] = Field(alias="errorCode", default=None,)
	runState: Optional[RunState | str] = Field(alias="runState", default=None,)

from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
from .run_state import RunState
