from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DailyInactiveUsersMetricCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DailyInactiveUsersMetric]] = Field(alias="value", default=None,)

from .daily_inactive_users_metric import DailyInactiveUsersMetric

