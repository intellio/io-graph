from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcOnPremisesConnectionHealthCheck(BaseModel):
	additionalDetail: Optional[str] = Field(default=None,alias="additionalDetail",)
	correlationId: Optional[str] = Field(default=None,alias="correlationId",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	errorType: Optional[CloudPcOnPremisesConnectionHealthCheckErrorType] = Field(default=None,alias="errorType",)
	recommendedAction: Optional[str] = Field(default=None,alias="recommendedAction",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	status: Optional[CloudPcOnPremisesConnectionStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cloud_pc_on_premises_connection_health_check_error_type import CloudPcOnPremisesConnectionHealthCheckErrorType
from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus

