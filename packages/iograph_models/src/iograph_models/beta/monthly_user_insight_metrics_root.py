from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MonthlyUserInsightMetricsRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activeUsers: Optional[list[ActiveUsersMetric]] = Field(alias="activeUsers", default=None,)
	authentications: Optional[list[AuthenticationsMetric]] = Field(alias="authentications", default=None,)
	inactiveUsers: Optional[list[MonthlyInactiveUsersMetric]] = Field(alias="inactiveUsers", default=None,)
	inactiveUsersByApplication: Optional[list[MonthlyInactiveUsersByApplicationMetric]] = Field(alias="inactiveUsersByApplication", default=None,)
	mfaCompletions: Optional[list[MfaCompletionMetric]] = Field(alias="mfaCompletions", default=None,)
	mfaRegisteredUsers: Optional[list[MfaUserCountMetric]] = Field(alias="mfaRegisteredUsers", default=None,)
	requests: Optional[list[UserRequestsMetric]] = Field(alias="requests", default=None,)
	signUps: Optional[list[UserSignUpMetric]] = Field(alias="signUps", default=None,)
	summary: Optional[list[InsightSummary]] = Field(alias="summary", default=None,)

from .active_users_metric import ActiveUsersMetric
from .authentications_metric import AuthenticationsMetric
from .monthly_inactive_users_metric import MonthlyInactiveUsersMetric
from .monthly_inactive_users_by_application_metric import MonthlyInactiveUsersByApplicationMetric
from .mfa_completion_metric import MfaCompletionMetric
from .mfa_user_count_metric import MfaUserCountMetric
from .user_requests_metric import UserRequestsMetric
from .user_sign_up_metric import UserSignUpMetric
from .insight_summary import InsightSummary

