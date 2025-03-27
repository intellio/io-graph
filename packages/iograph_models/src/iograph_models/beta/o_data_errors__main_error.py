from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ODataErrorsMainError(BaseModel):
	code: Optional[str] = Field(alias="code", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	target: Optional[str] = Field(alias="target", default=None,)
	details: Optional[list[ODataErrorsErrorDetails]] = Field(alias="details", default=None,)
	innerError: Optional[ODataErrorsInnerError] = Field(alias="innerError", default=None,)

from .o_data_errors__error_details import ODataErrorsErrorDetails
from .o_data_errors__inner_error import ODataErrorsInnerError

