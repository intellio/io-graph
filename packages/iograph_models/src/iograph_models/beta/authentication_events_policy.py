from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationEventsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	onSignupStart: SerializeAsAny[Optional[list[AuthenticationListener]]] = Field(alias="onSignupStart",default=None,)

from .authentication_listener import AuthenticationListener

