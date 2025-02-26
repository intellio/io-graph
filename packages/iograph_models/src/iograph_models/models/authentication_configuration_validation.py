from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationConfigurationValidation(BaseModel):
	errors: list[GenericError] = Field(alias="errors",)
	warnings: list[GenericError] = Field(alias="warnings",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .generic_error import GenericError
from .generic_error import GenericError

