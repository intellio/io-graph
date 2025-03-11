from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewHistoryInstance(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	downloadUri: Optional[str] = Field(alias="downloadUri",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	fulfilledDateTime: Optional[datetime] = Field(alias="fulfilledDateTime",default=None,)
	reviewHistoryPeriodEndDateTime: Optional[datetime] = Field(alias="reviewHistoryPeriodEndDateTime",default=None,)
	reviewHistoryPeriodStartDateTime: Optional[datetime] = Field(alias="reviewHistoryPeriodStartDateTime",default=None,)
	runDateTime: Optional[datetime] = Field(alias="runDateTime",default=None,)
	status: Optional[AccessReviewHistoryStatus | str] = Field(alias="status",default=None,)

from .access_review_history_status import AccessReviewHistoryStatus

