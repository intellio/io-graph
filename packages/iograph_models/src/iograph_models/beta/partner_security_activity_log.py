from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PartnerSecurityActivityLog(BaseModel):
	statusFrom: Optional[PartnerSecuritySecurityAlertStatus | str] = Field(alias="statusFrom", default=None,)
	statusTo: Optional[PartnerSecuritySecurityAlertStatus | str] = Field(alias="statusTo", default=None,)
	updatedBy: Optional[str] = Field(alias="updatedBy", default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .partner_security_security_alert_status import PartnerSecuritySecurityAlertStatus
