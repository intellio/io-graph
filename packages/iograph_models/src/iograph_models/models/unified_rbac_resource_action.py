from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRbacResourceAction(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	actionVerb: Optional[str] = Field(default=None,alias="actionVerb",)
	authenticationContextId: Optional[str] = Field(default=None,alias="authenticationContextId",)
	description: Optional[str] = Field(default=None,alias="description",)
	isAuthenticationContextSettable: Optional[bool] = Field(default=None,alias="isAuthenticationContextSettable",)
	name: Optional[str] = Field(default=None,alias="name",)
	resourceScopeId: Optional[str] = Field(default=None,alias="resourceScopeId",)


