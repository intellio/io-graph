from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcBulkActionSummary(BaseModel):
	failedCount: Optional[int] = Field(alias="failedCount", default=None,)
	inProgressCount: Optional[int] = Field(alias="inProgressCount", default=None,)
	notSupportedCount: Optional[int] = Field(alias="notSupportedCount", default=None,)
	pendingCount: Optional[int] = Field(alias="pendingCount", default=None,)
	successfulCount: Optional[int] = Field(alias="successfulCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

