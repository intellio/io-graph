from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UnifiedRbacResourceAction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.unifiedRbacResourceAction"] = Field(alias="@odata.type",)
	actionVerb: Optional[str] = Field(alias="actionVerb", default=None,)
	authenticationContextId: Optional[str] = Field(alias="authenticationContextId", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	isAuthenticationContextSettable: Optional[bool] = Field(alias="isAuthenticationContextSettable", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	resourceScopeId: Optional[str] = Field(alias="resourceScopeId", default=None,)

