from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessWebCategoryFilteringRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[NetworkaccessWebCategoryFilteringRule]] = Field(alias="value", default=None,)

from .networkaccess_web_category_filtering_rule import NetworkaccessWebCategoryFilteringRule
