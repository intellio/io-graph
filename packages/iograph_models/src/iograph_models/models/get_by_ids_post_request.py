from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_by_idsPostRequest(BaseModel):
	ids: list[str] = Field(alias="ids",)
	types: list[Optional[str]] = Field(alias="types",)


