from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PendingContentUpdate(BaseModel):
	queuedDateTime: Optional[datetime] = Field(default=None,alias="queuedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


