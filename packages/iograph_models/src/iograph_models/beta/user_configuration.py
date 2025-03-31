from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userConfiguration"] = Field(alias="@odata.type",)
	binaryData: Optional[str] = Field(alias="binaryData", default=None,)

