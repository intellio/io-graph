from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class CloudPcExternalPartnerSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcExternalPartnerSetting"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcExternalPartnerSetting")
	enableConnection: Optional[bool] = Field(alias="enableConnection", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	partnerId: Optional[str] = Field(alias="partnerId", default=None,)
	status: Optional[CloudPcExternalPartnerStatus | str] = Field(alias="status", default=None,)
	statusDetails: Optional[str] = Field(alias="statusDetails", default=None,)

from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus
