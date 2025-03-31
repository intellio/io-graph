from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ApprovalItemViewPoint(BaseModel):
	roles: Optional[list[ApproverRole | str]] = Field(alias="roles", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .approver_role import ApproverRole
