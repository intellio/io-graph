from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessRelatedWebCategory(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedWebCategory"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedWebCategory")
	webCategoryName: Optional[str] = Field(alias="webCategoryName", default=None,)

