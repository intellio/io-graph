from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ValidationResult(BaseModel):
	message: Optional[str] = Field(alias="message", default=None,)
	ruleName: Optional[str] = Field(alias="ruleName", default=None,)
	validationPassed: Optional[bool] = Field(alias="validationPassed", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

