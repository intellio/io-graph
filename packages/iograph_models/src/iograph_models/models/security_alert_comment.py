from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAlertComment(BaseModel):
	comment: Optional[str] = Field(default=None,alias="comment",)
	createdByDisplayName: Optional[str] = Field(default=None,alias="createdByDisplayName",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


