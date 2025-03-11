from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows_updates_add_members_by_idPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(alias="ids",default=None,)
	memberEntityType: Optional[str] = Field(alias="memberEntityType",default=None,)


