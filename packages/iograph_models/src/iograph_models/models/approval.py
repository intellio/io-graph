from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Approval(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	stages: Optional[list[ApprovalStage]] = Field(default=None,alias="stages",)

from .approval_stage import ApprovalStage

