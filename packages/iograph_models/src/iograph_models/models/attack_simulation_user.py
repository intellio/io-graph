from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AttackSimulationUser(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	email: Optional[str] = Field(default=None,alias="email",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


