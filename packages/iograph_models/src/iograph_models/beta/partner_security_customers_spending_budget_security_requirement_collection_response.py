from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnerSecurityCustomersSpendingBudgetSecurityRequirementCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PartnerSecurityCustomersSpendingBudgetSecurityRequirement]] = Field(alias="value", default=None,)

from .partner_security_customers_spending_budget_security_requirement import PartnerSecurityCustomersSpendingBudgetSecurityRequirement

