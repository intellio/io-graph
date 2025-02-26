from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IncompleteData(BaseModel):
	missingDataBeforeDateTime: Optional[datetime] = Field(default=None,alias="missingDataBeforeDateTime",)
	wasThrottled: Optional[bool] = Field(default=None,alias="wasThrottled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


