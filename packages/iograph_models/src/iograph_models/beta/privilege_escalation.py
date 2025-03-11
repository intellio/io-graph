from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegeEscalation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	actions: SerializeAsAny[Optional[list[AuthorizationSystemTypeAction]]] = Field(alias="actions",default=None,)
	resources: SerializeAsAny[Optional[list[AuthorizationSystemResource]]] = Field(alias="resources",default=None,)

from .authorization_system_type_action import AuthorizationSystemTypeAction
from .authorization_system_resource import AuthorizationSystemResource

