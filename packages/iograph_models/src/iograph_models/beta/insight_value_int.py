from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InsightValueInt(BaseModel):
	odata_type: Literal["#microsoft.graph.insightValueInt"] = Field(alias="@odata.type", default="#microsoft.graph.insightValueInt")
	value: Optional[int] = Field(alias="value", default=None,)

