from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OnPremisesConditionalAccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.onPremisesConditionalAccessSettings"] = Field(alias="@odata.type",)
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	excludedGroups: Optional[list[UUID]] = Field(alias="excludedGroups", default=None,)
	includedGroups: Optional[list[UUID]] = Field(alias="includedGroups", default=None,)
	overrideDefaultRule: Optional[bool] = Field(alias="overrideDefaultRule", default=None,)

