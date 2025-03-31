from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityInsiderRiskScopedUsersRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.insiderRiskScopedUsersRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.insiderRiskScopedUsersRecord")

