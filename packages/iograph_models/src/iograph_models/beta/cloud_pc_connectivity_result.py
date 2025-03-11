from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcConnectivityResult(BaseModel):
	failedHealthCheckItems: Optional[list[CloudPcHealthCheckItem]] = Field(alias="failedHealthCheckItems",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[CloudPcConnectivityStatus | str] = Field(alias="status",default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .cloud_pc_health_check_item import CloudPcHealthCheckItem
from .cloud_pc_connectivity_status import CloudPcConnectivityStatus

