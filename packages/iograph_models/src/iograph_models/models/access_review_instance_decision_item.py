from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accessReviewId: Optional[str] = Field(alias="accessReviewId",default=None,)
	appliedBy: Optional[UserIdentity] = Field(alias="appliedBy",default=None,)
	appliedDateTime: Optional[datetime] = Field(alias="appliedDateTime",default=None,)
	applyResult: Optional[str] = Field(alias="applyResult",default=None,)
	decision: Optional[str] = Field(alias="decision",default=None,)
	justification: Optional[str] = Field(alias="justification",default=None,)
	principal: SerializeAsAny[Optional[Identity]] = Field(alias="principal",default=None,)
	principalLink: Optional[str] = Field(alias="principalLink",default=None,)
	recommendation: Optional[str] = Field(alias="recommendation",default=None,)
	resource: SerializeAsAny[Optional[AccessReviewInstanceDecisionItemResource]] = Field(alias="resource",default=None,)
	resourceLink: Optional[str] = Field(alias="resourceLink",default=None,)
	reviewedBy: Optional[UserIdentity] = Field(alias="reviewedBy",default=None,)
	reviewedDateTime: Optional[datetime] = Field(alias="reviewedDateTime",default=None,)
	insights: SerializeAsAny[Optional[list[GovernanceInsight]]] = Field(alias="insights",default=None,)

from .user_identity import UserIdentity
from .identity import Identity
from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource
from .user_identity import UserIdentity
from .governance_insight import GovernanceInsight

