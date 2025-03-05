from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItem(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	accessReviewId: Optional[str] = Field(default=None,alias="accessReviewId",)
	appliedBy: Optional[UserIdentity] = Field(default=None,alias="appliedBy",)
	appliedDateTime: Optional[datetime] = Field(default=None,alias="appliedDateTime",)
	applyResult: Optional[str] = Field(default=None,alias="applyResult",)
	decision: Optional[str] = Field(default=None,alias="decision",)
	justification: Optional[str] = Field(default=None,alias="justification",)
	principal: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="principal",)
	principalLink: Optional[str] = Field(default=None,alias="principalLink",)
	recommendation: Optional[str] = Field(default=None,alias="recommendation",)
	resource: SerializeAsAny[Optional[AccessReviewInstanceDecisionItemResource]] = Field(default=None,alias="resource",)
	resourceLink: Optional[str] = Field(default=None,alias="resourceLink",)
	reviewedBy: Optional[UserIdentity] = Field(default=None,alias="reviewedBy",)
	reviewedDateTime: Optional[datetime] = Field(default=None,alias="reviewedDateTime",)
	insights: SerializeAsAny[Optional[list[GovernanceInsight]]] = Field(default=None,alias="insights",)

from .user_identity import UserIdentity
from .identity import Identity
from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource
from .user_identity import UserIdentity
from .governance_insight import GovernanceInsight

