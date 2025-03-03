from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ODataErrorsMainError(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	message: Optional[str] = Field(default=None,alias="message",)
	target: Optional[str] = Field(default=None,alias="target",)
	details: Optional[list[ODataErrorsErrorDetails]] = Field(default=None,alias="details",)
	innerError: Optional[ODataErrorsInnerError] = Field(default=None,alias="innerError",)

from .o_data_errors__error_details import ODataErrorsErrorDetails
from .o_data_errors__inner_error import ODataErrorsInnerError

