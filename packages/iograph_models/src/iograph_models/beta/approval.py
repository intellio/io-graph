from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Approval(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	steps: Optional[list[ApprovalStep]] = Field(alias="steps", default=None,)

from .approval_step import ApprovalStep

