from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class UserSignInInsight(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userSignInInsight"] = Field(alias="@odata.type", default="#microsoft.graph.userSignInInsight")
	insightCreatedDateTime: Optional[datetime] = Field(alias="insightCreatedDateTime", default=None,)
	lastSignInDateTime: Optional[datetime] = Field(alias="lastSignInDateTime", default=None,)

