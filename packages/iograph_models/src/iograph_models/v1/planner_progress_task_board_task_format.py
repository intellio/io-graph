from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PlannerProgressTaskBoardTaskFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.plannerProgressTaskBoardTaskFormat"] = Field(alias="@odata.type",)
	orderHint: Optional[str] = Field(alias="orderHint", default=None,)

