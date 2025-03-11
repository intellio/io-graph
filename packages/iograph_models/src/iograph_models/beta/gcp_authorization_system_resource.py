from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GcpAuthorizationSystemResource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	resourceType: Optional[str] = Field(alias="resourceType",default=None,)
	authorizationSystem: SerializeAsAny[Optional[AuthorizationSystem]] = Field(alias="authorizationSystem",default=None,)
	service: Optional[AuthorizationSystemTypeService] = Field(alias="service",default=None,)

from .authorization_system import AuthorizationSystem
from .authorization_system_type_service import AuthorizationSystemTypeService

