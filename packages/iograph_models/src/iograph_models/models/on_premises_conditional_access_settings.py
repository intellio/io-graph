from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesConditionalAccessSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	enabled: Optional[bool] = Field(default=None,alias="enabled",)
	excludedGroups: Optional[list[UUID]] = Field(default=None,alias="excludedGroups",)
	includedGroups: Optional[list[UUID]] = Field(default=None,alias="includedGroups",)
	overrideDefaultRule: Optional[bool] = Field(default=None,alias="overrideDefaultRule",)


