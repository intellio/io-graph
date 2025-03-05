from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceGroupBasedSubjectSet(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	groups: Optional[list[Group]] = Field(default=None,alias="groups",)

from .group import Group

