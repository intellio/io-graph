from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DailyUserInsightMetricsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.dailyUserInsightMetricsRoot"] = Field(alias="@odata.type",)
	activeUsers: Optional[list[ActiveUsersMetric]] = Field(alias="activeUsers", default=None,)
	authentications: Optional[list[AuthenticationsMetric]] = Field(alias="authentications", default=None,)
	inactiveUsers: Optional[list[DailyInactiveUsersMetric]] = Field(alias="inactiveUsers", default=None,)
	inactiveUsersByApplication: Optional[list[DailyInactiveUsersByApplicationMetric]] = Field(alias="inactiveUsersByApplication", default=None,)
	mfaCompletions: Optional[list[MfaCompletionMetric]] = Field(alias="mfaCompletions", default=None,)
	mfaTelecomFraud: Optional[list[MfaTelecomFraudMetric]] = Field(alias="mfaTelecomFraud", default=None,)
	signUps: Optional[list[UserSignUpMetric]] = Field(alias="signUps", default=None,)
	summary: Optional[list[InsightSummary]] = Field(alias="summary", default=None,)
	userCount: Optional[list[UserCountMetric]] = Field(alias="userCount", default=None,)

from .active_users_metric import ActiveUsersMetric
from .authentications_metric import AuthenticationsMetric
from .daily_inactive_users_metric import DailyInactiveUsersMetric
from .daily_inactive_users_by_application_metric import DailyInactiveUsersByApplicationMetric
from .mfa_completion_metric import MfaCompletionMetric
from .mfa_telecom_fraud_metric import MfaTelecomFraudMetric
from .user_sign_up_metric import UserSignUpMetric
from .insight_summary import InsightSummary
from .user_count_metric import UserCountMetric
