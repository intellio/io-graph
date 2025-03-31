from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PendingContentUpdate(BaseModel):
	queuedDateTime: Optional[datetime] = Field(alias="queuedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

