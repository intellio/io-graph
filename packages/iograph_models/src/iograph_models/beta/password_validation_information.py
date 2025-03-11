from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordValidationInformation(BaseModel):
	isValid: Optional[bool] = Field(alias="isValid",default=None,)
	validationResults: Optional[list[ValidationResult]] = Field(alias="validationResults",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .validation_result import ValidationResult

