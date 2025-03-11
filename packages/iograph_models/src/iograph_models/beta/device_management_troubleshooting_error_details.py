from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementTroubleshootingErrorDetails(BaseModel):
	context: Optional[str] = Field(alias="context",default=None,)
	failure: Optional[str] = Field(alias="failure",default=None,)
	failureDetails: Optional[str] = Field(alias="failureDetails",default=None,)
	remediation: Optional[str] = Field(alias="remediation",default=None,)
	resources: Optional[list[DeviceManagementTroubleshootingErrorResource]] = Field(alias="resources",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .device_management_troubleshooting_error_resource import DeviceManagementTroubleshootingErrorResource

