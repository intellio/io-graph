from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PasswordAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.passwordAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.passwordAuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	password: Optional[str] = Field(alias="password", default=None,)

