from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class BusinessScenarioPlanReference(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.businessScenarioPlanReference"] = Field(alias="@odata.type", default="#microsoft.graph.businessScenarioPlanReference")
	title: Optional[str] = Field(alias="title", default=None,)

