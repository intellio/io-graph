from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MembershipRuleEvaluationDetails(BaseModel):
	membershipRuleEvaluationDetails: Optional[ExpressionEvaluationDetails] = Field(alias="membershipRuleEvaluationDetails",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .expression_evaluation_details import ExpressionEvaluationDetails

