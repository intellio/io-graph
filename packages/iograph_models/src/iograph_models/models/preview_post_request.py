from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PreviewPostRequest(BaseModel):
	page: Optional[str] = Field(default=None,alias="page",)
	zoom: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

