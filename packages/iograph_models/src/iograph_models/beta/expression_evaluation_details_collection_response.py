from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExpressionEvaluationDetailsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ExpressionEvaluationDetails]] = Field(alias="value",default=None,)

from .expression_evaluation_details import ExpressionEvaluationDetails

