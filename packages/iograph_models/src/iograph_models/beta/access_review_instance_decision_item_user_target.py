from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItemUserTarget(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)


