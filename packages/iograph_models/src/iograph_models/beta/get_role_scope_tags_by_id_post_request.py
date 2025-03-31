from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_role_scope_tags_by_idPostRequest(BaseModel):
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)

