from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PartnerSecurityPartnerSecurityAlertCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PartnerSecurityPartnerSecurityAlert]] = Field(alias="value", default=None,)

from .partner_security_partner_security_alert import PartnerSecurityPartnerSecurityAlert
