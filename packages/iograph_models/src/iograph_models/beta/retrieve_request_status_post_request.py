from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Retrieve_request_statusPostRequest(BaseModel):
	entityId: Optional[str] = Field(alias="entityId", default=None,)
	entityType: Optional[str] = Field(alias="entityType", default=None,)


