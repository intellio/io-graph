from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WhatIfAuthenticationContext(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	authenticationContext: Optional[str] = Field(alias="authenticationContext",default=None,)


