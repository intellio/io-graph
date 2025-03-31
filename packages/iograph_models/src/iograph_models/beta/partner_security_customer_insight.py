from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PartnerSecurityCustomerInsight(BaseModel):
	mfa: Optional[PartnerSecurityCustomerMfaInsight] = Field(alias="mfa", default=None,)
	tenantId: Optional[str] = Field(alias="tenantId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .partner_security_customer_mfa_insight import PartnerSecurityCustomerMfaInsight
