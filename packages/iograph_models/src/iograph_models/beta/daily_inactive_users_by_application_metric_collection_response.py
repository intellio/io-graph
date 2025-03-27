from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DailyInactiveUsersByApplicationMetricCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DailyInactiveUsersByApplicationMetric]] = Field(alias="value", default=None,)

from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric

