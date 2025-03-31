from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ResourceOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.resourceOperation"] = Field(alias="@odata.type",)
	actionName: Optional[str] = Field(alias="actionName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	resourceName: Optional[str] = Field(alias="resourceName", default=None,)

