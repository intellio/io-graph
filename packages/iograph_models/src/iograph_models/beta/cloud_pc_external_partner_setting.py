from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcExternalPartnerSetting(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	enableConnection: Optional[bool] = Field(alias="enableConnection", default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime", default=None,)
	partnerId: Optional[str] = Field(alias="partnerId", default=None,)
	status: Optional[CloudPcExternalPartnerStatus | str] = Field(alias="status", default=None,)
	statusDetails: Optional[str] = Field(alias="statusDetails", default=None,)

from .cloud_pc_external_partner_status import CloudPcExternalPartnerStatus

