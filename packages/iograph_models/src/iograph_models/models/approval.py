from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Approval(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	stages: Optional[list[ApprovalStage]] = Field(alias="stages",default=None,)

from .approval_stage import ApprovalStage

