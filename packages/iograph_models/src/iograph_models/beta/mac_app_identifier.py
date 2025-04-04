from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MacAppIdentifier(BaseModel):
	odata_type: Literal["#microsoft.graph.macAppIdentifier"] = Field(alias="@odata.type", default="#microsoft.graph.macAppIdentifier")
	bundleId: Optional[str] = Field(alias="bundleId", default=None,)

