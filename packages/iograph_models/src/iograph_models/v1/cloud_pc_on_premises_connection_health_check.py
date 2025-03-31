from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcOnPremisesConnectionHealthCheck(BaseModel):
	additionalDetail: Optional[str] = Field(alias="additionalDetail", default=None,)
	correlationId: Optional[str] = Field(alias="correlationId", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	errorType: Optional[CloudPcOnPremisesConnectionHealthCheckErrorType | str] = Field(alias="errorType", default=None,)
	recommendedAction: Optional[str] = Field(alias="recommendedAction", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[CloudPcOnPremisesConnectionStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_on_premises_connection_health_check_error_type import CloudPcOnPremisesConnectionHealthCheckErrorType
from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
