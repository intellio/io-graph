from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessReviewInstanceDecisionItemUserTarget(BaseModel):
	odata_type: Literal["#microsoft.graph.accessReviewInstanceDecisionItemUserTarget"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewInstanceDecisionItemUserTarget")
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

