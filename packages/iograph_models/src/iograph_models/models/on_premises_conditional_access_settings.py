from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesConditionalAccessSettings(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	enabled: Optional[bool] = Field(default=None,alias="enabled",)
	excludedGroups: list[UUID] = Field(alias="excludedGroups",)
	includedGroups: list[UUID] = Field(alias="includedGroups",)
	overrideDefaultRule: Optional[bool] = Field(default=None,alias="overrideDefaultRule",)


