from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PreviewPostRequest(BaseModel):
	page: Optional[str] = Field(alias="page", default=None,)
	zoom: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
