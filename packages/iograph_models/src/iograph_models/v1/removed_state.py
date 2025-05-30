from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RemovedState(BaseModel):
	reason: Optional[str] = Field(alias="reason", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

