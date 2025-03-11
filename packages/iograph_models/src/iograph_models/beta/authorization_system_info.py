from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthorizationSystemInfo(BaseModel):
	authorizationSystemType: Optional[AuthorizationSystemType | str] = Field(alias="authorizationSystemType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authorization_system_type import AuthorizationSystemType

