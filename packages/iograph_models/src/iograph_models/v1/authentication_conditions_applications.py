from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationConditionsApplications(BaseModel):
	includeApplications: Optional[list[AuthenticationConditionApplication]] = Field(alias="includeApplications", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_condition_application import AuthenticationConditionApplication
