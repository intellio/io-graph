from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserInsightsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userInsightsRoot"] = Field(alias="@odata.type",)
	daily: Optional[DailyUserInsightMetricsRoot] = Field(alias="daily", default=None,)
	monthly: Optional[MonthlyUserInsightMetricsRoot] = Field(alias="monthly", default=None,)

from .daily_user_insight_metrics_root import DailyUserInsightMetricsRoot
from .monthly_user_insight_metrics_root import MonthlyUserInsightMetricsRoot
