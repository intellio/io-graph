from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcRemoteActionResult(BaseModel):
	actionName: Optional[str] = Field(alias="actionName", default=None,)
	actionState: Optional[ActionState | str] = Field(alias="actionState", default=None,)
	cloudPcId: Optional[str] = Field(alias="cloudPcId", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	statusDetail: Optional[CloudPcStatusDetail] = Field(alias="statusDetail", default=None,)
	statusDetails: Optional[CloudPcStatusDetails] = Field(alias="statusDetails", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .action_state import ActionState
from .cloud_pc_status_detail import CloudPcStatusDetail
from .cloud_pc_status_details import CloudPcStatusDetails

