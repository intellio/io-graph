from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Confirm_compromisedPostRequest(BaseModel):
	userIds: Optional[list[str]] = Field(default=None,alias="userIds",)


