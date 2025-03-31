from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AppleVppTokenTroubleshootingEvent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.appleVppTokenTroubleshootingEvent"] = Field(alias="@odata.type",)
	additionalInformation: Optional[list[KeyValuePair]] = Field(alias="additionalInformation", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime", default=None,)
	eventName: Optional[str] = Field(alias="eventName", default=None,)
	troubleshootingErrorDetails: Optional[DeviceManagementTroubleshootingErrorDetails] = Field(alias="troubleshootingErrorDetails", default=None,)
	tokenId: Optional[str] = Field(alias="tokenId", default=None,)

from .key_value_pair import KeyValuePair
from .device_management_troubleshooting_error_details import DeviceManagementTroubleshootingErrorDetails
