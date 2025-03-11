from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationBehaviors(BaseModel):
	blockAzureADGraphAccess: Optional[bool] = Field(alias="blockAzureADGraphAccess",default=None,)
	removeUnverifiedEmailClaim: Optional[bool] = Field(alias="removeUnverifiedEmailClaim",default=None,)
	requireClientServicePrincipal: Optional[bool] = Field(alias="requireClientServicePrincipal",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


