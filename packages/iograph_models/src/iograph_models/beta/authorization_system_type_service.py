from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystemTypeService(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actions: SerializeAsAny[Optional[list[AuthorizationSystemTypeAction]]] = Field(alias="actions",default=None,)

from .authorization_system_type_action import AuthorizationSystemTypeAction

