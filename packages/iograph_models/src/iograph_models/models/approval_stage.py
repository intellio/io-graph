from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ApprovalStage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	assignedToMe: Optional[bool] = Field(default=None,alias="assignedToMe",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	justification: Optional[str] = Field(default=None,alias="justification",)
	reviewedBy: Optional[Identity] = Field(default=None,alias="reviewedBy",)
	reviewedDateTime: Optional[datetime] = Field(default=None,alias="reviewedDateTime",)
	reviewResult: Optional[str] = Field(default=None,alias="reviewResult",)
	status: Optional[str] = Field(default=None,alias="status",)

from .identity import Identity

