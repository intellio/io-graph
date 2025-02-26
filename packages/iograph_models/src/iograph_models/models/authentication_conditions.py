from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationConditions(BaseModel):
	applications: Optional[AuthenticationConditionsApplications] = Field(default=None,alias="applications",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .authentication_conditions_applications import AuthenticationConditionsApplications

