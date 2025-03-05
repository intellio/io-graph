from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecureScoreControlStateUpdate(BaseModel):
	assignedTo: Optional[str] = Field(default=None,alias="assignedTo",)
	comment: Optional[str] = Field(default=None,alias="comment",)
	state: Optional[str] = Field(default=None,alias="state",)
	updatedBy: Optional[str] = Field(default=None,alias="updatedBy",)
	updatedDateTime: Optional[datetime] = Field(default=None,alias="updatedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


