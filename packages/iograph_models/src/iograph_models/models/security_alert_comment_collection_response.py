from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAlertCommentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityAlertComment]] = Field(default=None,alias="value",)

from .security_alert_comment import SecurityAlertComment

