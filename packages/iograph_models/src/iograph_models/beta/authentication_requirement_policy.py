from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationRequirementPolicy(BaseModel):
	detail: Optional[str] = Field(alias="detail", default=None,)
	requirementProvider: Optional[RequirementProvider | str] = Field(alias="requirementProvider", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .requirement_provider import RequirementProvider
