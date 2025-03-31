from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySubcategoryTemplateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecuritySubcategoryTemplate]] = Field(alias="value", default=None,)

from .security_subcategory_template import SecuritySubcategoryTemplate
