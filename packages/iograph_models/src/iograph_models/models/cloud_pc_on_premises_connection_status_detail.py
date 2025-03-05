from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcOnPremisesConnectionStatusDetail(BaseModel):
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	healthChecks: Optional[list[CloudPcOnPremisesConnectionHealthCheck]] = Field(default=None,alias="healthChecks",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cloud_pc_on_premises_connection_health_check import CloudPcOnPremisesConnectionHealthCheck

