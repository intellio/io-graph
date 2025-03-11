from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationContext(BaseModel):
	detail: Optional[AuthenticationContextDetail | str] = Field(alias="detail",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authentication_context_detail import AuthenticationContextDetail

