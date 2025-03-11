from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GovernancePolicy(BaseModel):
	decisionMakerCriteria: SerializeAsAny[Optional[list[GovernanceCriteria]]] = Field(alias="decisionMakerCriteria",default=None,)
	notificationPolicy: Optional[GovernanceNotificationPolicy] = Field(alias="notificationPolicy",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .governance_criteria import GovernanceCriteria
from .governance_notification_policy import GovernanceNotificationPolicy

