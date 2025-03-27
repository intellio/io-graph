from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class WhatIfAuthenticationContext(BaseModel):
	odata_type: Literal["#microsoft.graph.whatIfAuthenticationContext"] = Field(alias="@odata.type", default="#microsoft.graph.whatIfAuthenticationContext")
	authenticationContext: Optional[str] = Field(alias="authenticationContext", default=None,)


