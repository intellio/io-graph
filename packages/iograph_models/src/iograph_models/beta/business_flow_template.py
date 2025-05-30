from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class BusinessFlowTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.businessFlowTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.businessFlowTemplate")
	displayName: Optional[str] = Field(alias="displayName", default=None,)

