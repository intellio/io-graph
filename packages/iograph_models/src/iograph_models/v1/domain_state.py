from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class DomainState(BaseModel):
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	operation: Optional[str] = Field(alias="operation", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

