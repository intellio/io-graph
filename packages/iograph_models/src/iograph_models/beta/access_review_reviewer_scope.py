from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessReviewReviewerScope(BaseModel):
	odata_type: Literal["#microsoft.graph.accessReviewReviewerScope"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewReviewerScope")
	query: Optional[str] = Field(alias="query", default=None,)
	queryRoot: Optional[str] = Field(alias="queryRoot", default=None,)
	queryType: Optional[str] = Field(alias="queryType", default=None,)

