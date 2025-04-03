from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EducationGradingCategory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.educationGradingCategory"] = Field(alias="@odata.type", default="#microsoft.graph.educationGradingCategory")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	percentageWeight: Optional[int] = Field(alias="percentageWeight", default=None,)

