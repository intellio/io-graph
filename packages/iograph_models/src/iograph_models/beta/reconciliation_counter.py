from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ReconciliationCounter(BaseModel):
	correlatedObjectCount: Optional[int] = Field(alias="correlatedObjectCount", default=None,)
	sourceObjectCount: Optional[int] = Field(alias="sourceObjectCount", default=None,)
	targetObjectCount: Optional[int] = Field(alias="targetObjectCount", default=None,)
	uncorrelatedObjectCount: Optional[int] = Field(alias="uncorrelatedObjectCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

