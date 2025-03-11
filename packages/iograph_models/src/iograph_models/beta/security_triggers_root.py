from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTriggersRoot(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	retentionEvents: Optional[list[SecurityRetentionEvent]] = Field(alias="retentionEvents",default=None,)

from .security_retention_event import SecurityRetentionEvent

