from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UsageRight(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.usageRight"] = Field(alias="@odata.type", default="#microsoft.graph.usageRight")
	catalogId: Optional[str] = Field(alias="catalogId", default=None,)
	serviceIdentifier: Optional[str] = Field(alias="serviceIdentifier", default=None,)
	state: Optional[UsageRightState | str] = Field(alias="state", default=None,)

from .usage_right_state import UsageRightState
