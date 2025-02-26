from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_remove_holdPostRequest(BaseModel):
	ids: list[Optional[str]] = Field(alias="ids",)


