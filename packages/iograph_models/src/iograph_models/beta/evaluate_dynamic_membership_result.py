from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EvaluateDynamicMembershipResult(BaseModel):
	membershipRule: Optional[str] = Field(alias="membershipRule", default=None,)
	membershipRuleEvaluationDetails: Optional[ExpressionEvaluationDetails] = Field(alias="membershipRuleEvaluationDetails", default=None,)
	membershipRuleEvaluationResult: Optional[bool] = Field(alias="membershipRuleEvaluationResult", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .expression_evaluation_details import ExpressionEvaluationDetails

