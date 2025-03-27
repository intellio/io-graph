from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerSecurityPartnerSecurityScore(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	currentScore: float | str | ReferenceNumeric
	lastRefreshDateTime: Optional[datetime] = Field(alias="lastRefreshDateTime", default=None,)
	maxScore: float | str | ReferenceNumeric
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	customerInsights: Optional[list[PartnerSecurityCustomerInsight]] = Field(alias="customerInsights", default=None,)
	history: Optional[list[PartnerSecuritySecurityScoreHistory]] = Field(alias="history", default=None,)
	requirements: Optional[list[Annotated[Union[PartnerSecurityAdminsMfaEnforcedSecurityRequirement, PartnerSecurityCustomersMfaEnforcedSecurityRequirement, PartnerSecurityCustomersSpendingBudgetSecurityRequirement, PartnerSecurityResponseTimeSecurityRequirement],Field(discriminator="odata_type")]]] = Field(alias="requirements", default=None,)

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .partner_security_customer_insight import PartnerSecurityCustomerInsight
from .partner_security_security_score_history import PartnerSecuritySecurityScoreHistory
from .partner_security_admins_mfa_enforced_security_requirement import PartnerSecurityAdminsMfaEnforcedSecurityRequirement
from .partner_security_customers_mfa_enforced_security_requirement import PartnerSecurityCustomersMfaEnforcedSecurityRequirement
from .partner_security_customers_spending_budget_security_requirement import PartnerSecurityCustomersSpendingBudgetSecurityRequirement
from .partner_security_response_time_security_requirement import PartnerSecurityResponseTimeSecurityRequirement

