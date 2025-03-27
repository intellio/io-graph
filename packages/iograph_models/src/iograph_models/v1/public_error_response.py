from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PublicErrorResponse(BaseModel):
	error: Optional[PublicError] = Field(alias="error", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .public_error import PublicError

