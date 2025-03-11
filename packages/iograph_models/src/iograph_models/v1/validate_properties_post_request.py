from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_propertiesPostRequest(BaseModel):
	entityType: Optional[str] = Field(alias="entityType",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	mailNickname: Optional[str] = Field(alias="mailNickname",default=None,)
	onBehalfOfUserId: Optional[UUID] = Field(alias="onBehalfOfUserId",default=None,)


