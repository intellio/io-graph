from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UnknownSource(BaseModel):
	identityProviderType: Optional[str] = Field(alias="identityProviderType", default=None,)
	odata_type: Literal["#microsoft.graph.unknownSource"] = Field(alias="@odata.type", default="#microsoft.graph.unknownSource")

