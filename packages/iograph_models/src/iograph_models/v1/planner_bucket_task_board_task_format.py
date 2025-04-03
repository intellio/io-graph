from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerBucketTaskBoardTaskFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerBucketTaskBoardTaskFormat"] = Field(alias="@odata.type", default="#microsoft.graph.plannerBucketTaskBoardTaskFormat")
	orderHint: Optional[str] = Field(alias="orderHint", default=None,)

