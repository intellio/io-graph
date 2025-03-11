from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnumeratedAccountsWithAccess(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accounts: SerializeAsAny[Optional[list[AuthorizationSystem]]] = Field(alias="accounts",default=None,)

from .authorization_system import AuthorizationSystem

