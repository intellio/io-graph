from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PartnerSecurityPartnerSecurity(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.partner.security.partnerSecurity"] = Field(alias="@odata.type",)
	securityAlerts: Optional[list[PartnerSecurityPartnerSecurityAlert]] = Field(alias="securityAlerts", default=None,)
	securityScore: Optional[PartnerSecurityPartnerSecurityScore] = Field(alias="securityScore", default=None,)

from .partner_security_partner_security_alert import PartnerSecurityPartnerSecurityAlert
from .partner_security_partner_security_score import PartnerSecurityPartnerSecurityScore
