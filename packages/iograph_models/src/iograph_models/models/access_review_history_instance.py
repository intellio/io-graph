from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewHistoryInstance(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	downloadUri: Optional[str] = Field(default=None,alias="downloadUri",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	fulfilledDateTime: Optional[datetime] = Field(default=None,alias="fulfilledDateTime",)
	reviewHistoryPeriodEndDateTime: Optional[datetime] = Field(default=None,alias="reviewHistoryPeriodEndDateTime",)
	reviewHistoryPeriodStartDateTime: Optional[datetime] = Field(default=None,alias="reviewHistoryPeriodStartDateTime",)
	runDateTime: Optional[datetime] = Field(default=None,alias="runDateTime",)
	status: Optional[AccessReviewHistoryStatus] = Field(default=None,alias="status",)

from .access_review_history_status import AccessReviewHistoryStatus

