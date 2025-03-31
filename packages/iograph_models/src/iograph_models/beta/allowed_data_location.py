from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AllowedDataLocation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.allowedDataLocation"] = Field(alias="@odata.type",)
	appId: Optional[str] = Field(alias="appId", default=None,)
	domain: Optional[str] = Field(alias="domain", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	location: Optional[str] = Field(alias="location", default=None,)

