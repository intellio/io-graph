from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class EmailAuthenticationMethod(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.emailAuthenticationMethod"] = Field(alias="@odata.type", default="#microsoft.graph.emailAuthenticationMethod")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)

