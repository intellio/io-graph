from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DomainState(BaseModel):
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	operation: Optional[str] = Field(default=None,alias="operation",)
	status: Optional[str] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


