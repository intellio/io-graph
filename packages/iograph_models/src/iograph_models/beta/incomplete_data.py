from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IncompleteData(BaseModel):
	missingDataBeforeDateTime: Optional[datetime] = Field(alias="missingDataBeforeDateTime", default=None,)
	wasThrottled: Optional[bool] = Field(alias="wasThrottled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

