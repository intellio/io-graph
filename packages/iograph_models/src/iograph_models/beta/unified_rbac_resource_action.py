from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UnifiedRbacResourceAction(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionVerb: Optional[str] = Field(alias="actionVerb",default=None,)
	authenticationContextId: Optional[str] = Field(alias="authenticationContextId",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	isAuthenticationContextSettable: Optional[bool] = Field(alias="isAuthenticationContextSettable",default=None,)
	isPrivileged: Optional[bool] = Field(alias="isPrivileged",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	resourceScopeId: Optional[str] = Field(alias="resourceScopeId",default=None,)
	authenticationContext: Optional[AuthenticationContextClassReference] = Field(alias="authenticationContext",default=None,)
	resourceScope: Optional[UnifiedRbacResourceScope] = Field(alias="resourceScope",default=None,)

from .authentication_context_class_reference import AuthenticationContextClassReference
from .unified_rbac_resource_scope import UnifiedRbacResourceScope

