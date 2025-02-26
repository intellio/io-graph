from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Copy_to_default_content_locationPostRequest(BaseModel):
	sourceFile: Optional[ItemReference] = Field(default=None,alias="sourceFile",)
	destinationFileName: Optional[str] = Field(default=None,alias="destinationFileName",)

from .item_reference import ItemReference

