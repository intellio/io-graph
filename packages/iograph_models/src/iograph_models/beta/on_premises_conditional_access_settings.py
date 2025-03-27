from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesConditionalAccessSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	excludedGroups: Optional[list[UUID]] = Field(alias="excludedGroups", default=None,)
	includedGroups: Optional[list[UUID]] = Field(alias="includedGroups", default=None,)
	overrideDefaultRule: Optional[bool] = Field(alias="overrideDefaultRule", default=None,)


