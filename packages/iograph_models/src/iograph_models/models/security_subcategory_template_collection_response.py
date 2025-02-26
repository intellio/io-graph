from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySubcategoryTemplateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecuritySubcategoryTemplate] = Field(alias="value",)

from .security_subcategory_template import SecuritySubcategoryTemplate

