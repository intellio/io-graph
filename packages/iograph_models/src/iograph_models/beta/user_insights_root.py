from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserInsightsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	daily: Optional[DailyUserInsightMetricsRoot] = Field(alias="daily", default=None,)
	monthly: Optional[MonthlyUserInsightMetricsRoot] = Field(alias="monthly", default=None,)

from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot

