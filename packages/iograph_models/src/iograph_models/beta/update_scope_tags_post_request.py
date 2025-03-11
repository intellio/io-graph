from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_scope_tagsPostRequest(BaseModel):
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds",default=None,)


