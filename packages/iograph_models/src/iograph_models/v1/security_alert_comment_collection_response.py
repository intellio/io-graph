from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAlertCommentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityAlertComment]] = Field(alias="value", default=None,)

from .security_alert_comment import SecurityAlertComment
