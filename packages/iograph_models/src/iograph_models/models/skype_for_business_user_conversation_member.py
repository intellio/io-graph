from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SkypeForBusinessUserConversationMember(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	roles: Optional[list[str]] = Field(default=None,alias="roles",)
	visibleHistoryStartDateTime: Optional[datetime] = Field(default=None,alias="visibleHistoryStartDateTime",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	userId: Optional[str] = Field(default=None,alias="userId",)


