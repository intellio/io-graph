from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecureScoreControlStateUpdate(BaseModel):
	assignedTo: Optional[str] = Field(alias="assignedTo", default=None,)
	comment: Optional[str] = Field(alias="comment", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	updatedBy: Optional[str] = Field(alias="updatedBy", default=None,)
	updatedDateTime: Optional[datetime] = Field(alias="updatedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

