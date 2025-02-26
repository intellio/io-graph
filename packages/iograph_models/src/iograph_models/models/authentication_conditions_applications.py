from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationConditionsApplications(BaseModel):
	includeApplications: list[AuthenticationConditionApplication] = Field(alias="includeApplications",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_condition_application import AuthenticationConditionApplication

