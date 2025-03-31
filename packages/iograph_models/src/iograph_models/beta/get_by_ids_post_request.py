from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_by_idsPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(alias="ids", default=None,)
	types: Optional[list[str]] = Field(alias="types", default=None,)

