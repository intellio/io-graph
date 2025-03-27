from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcOnPremisesConnectionStatusDetail(BaseModel):
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	healthChecks: Optional[list[CloudPcOnPremisesConnectionHealthCheck]] = Field(alias="healthChecks", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_on_premises_connection_health_check import CloudPcOnPremisesConnectionHealthCheck

