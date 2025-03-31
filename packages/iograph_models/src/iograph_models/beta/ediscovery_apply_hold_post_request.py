from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Ediscovery_apply_holdPostRequest(BaseModel):
	ids: Optional[list[str]] = Field(alias="ids", default=None,)

