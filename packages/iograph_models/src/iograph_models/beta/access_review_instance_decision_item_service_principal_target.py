from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessReviewInstanceDecisionItemServicePrincipalTarget(BaseModel):
	odata_type: Literal["#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalTarget"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalTarget")
	appId: Optional[str] = Field(alias="appId", default=None,)
	servicePrincipalDisplayName: Optional[str] = Field(alias="servicePrincipalDisplayName", default=None,)
	servicePrincipalId: Optional[str] = Field(alias="servicePrincipalId", default=None,)

