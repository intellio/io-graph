from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ODataErrorsODataError(BaseModel):
	error: Optional[ODataErrorsMainError] = Field(alias="error",default=None,)

from .o_data_errors__main_error import ODataErrorsMainError

