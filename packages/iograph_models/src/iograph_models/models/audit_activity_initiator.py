from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditActivityInitiator(BaseModel):
	app: Optional[AppIdentity] = Field(default=None,alias="app",)
	user: Optional[UserIdentity] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .app_identity import AppIdentity
from .user_identity import UserIdentity

