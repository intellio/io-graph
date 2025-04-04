from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AppHostedMediaConfig(BaseModel):
	odata_type: Literal["#microsoft.graph.appHostedMediaConfig"] = Field(alias="@odata.type", default="#microsoft.graph.appHostedMediaConfig")
	blob: Optional[str] = Field(alias="blob", default=None,)

