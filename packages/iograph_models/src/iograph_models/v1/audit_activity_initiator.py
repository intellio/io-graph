from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuditActivityInitiator(BaseModel):
	app: Optional[AppIdentity] = Field(alias="app", default=None,)
	user: Optional[UserIdentity] = Field(alias="user", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .app_identity import AppIdentity
from .user_identity import UserIdentity

