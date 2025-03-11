from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystemTypeActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[AuthorizationSystemTypeAction]]] = Field(alias="value",default=None,)

from .authorization_system_type_action import AuthorizationSystemTypeAction

