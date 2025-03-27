from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationConditions(BaseModel):
	applications: Optional[AuthenticationConditionsApplications] = Field(alias="applications", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .authentication_conditions_applications import AuthenticationConditionsApplications

