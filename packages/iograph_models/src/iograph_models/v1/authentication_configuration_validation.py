from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationConfigurationValidation(BaseModel):
	errors: Optional[list[GenericError]] = Field(alias="errors", default=None,)
	warnings: Optional[list[GenericError]] = Field(alias="warnings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .generic_error import GenericError
from .generic_error import GenericError

