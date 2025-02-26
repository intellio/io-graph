from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IdentityGovernanceGroupBasedSubjectSet(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	groups: list[Group] = Field(alias="groups",)

from .group import Group

