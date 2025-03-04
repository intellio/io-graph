from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationBehaviors(BaseModel):
	blockAzureADGraphAccess: Optional[bool] = Field(default=None,alias="blockAzureADGraphAccess",)
	removeUnverifiedEmailClaim: Optional[bool] = Field(default=None,alias="removeUnverifiedEmailClaim",)
	requireClientServicePrincipal: Optional[bool] = Field(default=None,alias="requireClientServicePrincipal",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


