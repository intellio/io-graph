from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_propertiesPostRequest(BaseModel):
	entityType: Optional[str] = Field(default=None,alias="entityType",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	mailNickname: Optional[str] = Field(default=None,alias="mailNickname",)
	onBehalfOfUserId: Optional[UUID] = Field(default=None,alias="onBehalfOfUserId",)


