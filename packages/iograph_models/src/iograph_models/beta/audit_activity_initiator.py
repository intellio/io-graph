from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuditActivityInitiator(BaseModel):
	app: Optional[AppIdentity] = Field(alias="app", default=None,)
	user: Optional[AuditUserIdentity] = Field(alias="user", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .app_identity import AppIdentity
from .audit_user_identity import AuditUserIdentity
