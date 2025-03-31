from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SingleUser(BaseModel):
	isBackup: Optional[bool] = Field(alias="isBackup", default=None,)
	odata_type: Literal["#microsoft.graph.singleUser"] = Field(alias="@odata.type", default="#microsoft.graph.singleUser")
	description: Optional[str] = Field(alias="description", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)

