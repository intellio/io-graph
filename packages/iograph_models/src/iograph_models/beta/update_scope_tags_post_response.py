from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Update_scope_tagsPostResponse(BaseModel):
	value: Optional[str] = Field(alias="value", default=None,)


