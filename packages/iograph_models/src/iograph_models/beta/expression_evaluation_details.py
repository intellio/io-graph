from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExpressionEvaluationDetails(BaseModel):
	expression: Optional[str] = Field(alias="expression",default=None,)
	expressionEvaluationDetails: Optional[list[ExpressionEvaluationDetails]] = Field(alias="expressionEvaluationDetails",default=None,)
	expressionResult: Optional[bool] = Field(alias="expressionResult",default=None,)
	propertyToEvaluate: Optional[PropertyToEvaluate] = Field(alias="propertyToEvaluate",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .property_to_evaluate import PropertyToEvaluate

