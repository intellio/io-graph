from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MfaUserCountMetricCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MfaUserCountMetric]] = Field(alias="value", default=None,)

from .mfa_user_count_metric import MfaUserCountMetric
