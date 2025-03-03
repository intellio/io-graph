from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationConfigurationValidation(BaseModel):
	errors: Optional[list[GenericError]] = Field(default=None,alias="errors",)
	warnings: Optional[list[GenericError]] = Field(default=None,alias="warnings",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .generic_error import GenericError
from .generic_error import GenericError

