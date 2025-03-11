from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AadUserConversationMember(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	roles: Optional[list[str]] = Field(alias="roles",default=None,)
	visibleHistoryStartDateTime: Optional[datetime] = Field(alias="visibleHistoryStartDateTime",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	user: Optional[User] = Field(alias="user",default=None,)

from .user import User

