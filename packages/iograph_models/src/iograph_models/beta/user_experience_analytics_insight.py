from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsInsight(BaseModel):
	insightId: Optional[str] = Field(alias="insightId", default=None,)
	severity: Optional[UserExperienceAnalyticsInsightSeverity | str] = Field(alias="severity", default=None,)
	userExperienceAnalyticsMetricId: Optional[str] = Field(alias="userExperienceAnalyticsMetricId", default=None,)
	values: Optional[list[Annotated[Union[InsightValueDouble, InsightValueInt],Field(discriminator="odata_type")]]] = Field(alias="values", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .user_experience_analytics_insight_severity import UserExperienceAnalyticsInsightSeverity
from .insight_value_double import InsightValueDouble
from .insight_value_int import InsightValueInt

