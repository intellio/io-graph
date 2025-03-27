from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContinuousAccessEvaluationPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	groups: Optional[list[str]] = Field(alias="groups", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	migrate: Optional[bool] = Field(alias="migrate", default=None,)
	users: Optional[list[str]] = Field(alias="users", default=None,)


