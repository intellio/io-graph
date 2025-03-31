from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Has_custom_role_scope_tagGetResponse(BaseModel):
	value: Optional[bool] = Field(alias="value", default=None,)

