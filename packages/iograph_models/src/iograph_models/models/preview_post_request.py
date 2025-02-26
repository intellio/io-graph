from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PreviewPostRequest(BaseModel):
	page: Optional[str] = Field(default=None,alias="page",)
	zoom: Optional[float] | Optional[str] | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

