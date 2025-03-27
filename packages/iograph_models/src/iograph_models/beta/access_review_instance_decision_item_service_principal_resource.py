from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItemServicePrincipalResource(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource")
	appId: Optional[str] = Field(alias="appId", default=None,)


