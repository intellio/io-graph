from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Approval(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.approval"] = Field(alias="@odata.type", default="#microsoft.graph.approval")
	steps: Optional[list[ApprovalStep]] = Field(alias="steps", default=None,)

from .approval_step import ApprovalStep
