from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityRetentionEventStatus(BaseModel):
	error: Optional[PublicError] = Field(alias="error", default=None,)
	status: Optional[SecurityEventStatusType | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .public_error import PublicError
from .security_event_status_type import SecurityEventStatusType
