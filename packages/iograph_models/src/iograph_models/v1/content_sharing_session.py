from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ContentSharingSession(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.contentSharingSession"] = Field(alias="@odata.type",)

