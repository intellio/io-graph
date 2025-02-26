from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewInstanceDecisionItemAzureRoleResource(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[str] = Field(default=None,alias="id",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	scope: Optional[AccessReviewInstanceDecisionItemResource] = Field(default=None,alias="scope",)

from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

