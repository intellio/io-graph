from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItemAzureRoleResource(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	scope: SerializeAsAny[Optional[AccessReviewInstanceDecisionItemResource]] = Field(alias="scope",default=None,)

from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

