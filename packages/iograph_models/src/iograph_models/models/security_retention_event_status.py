from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityRetentionEventStatus(BaseModel):
	error: Optional[PublicError] = Field(default=None,alias="error",)
	status: Optional[SecurityEventStatusType] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .public_error import PublicError
from .security_event_status_type import SecurityEventStatusType

