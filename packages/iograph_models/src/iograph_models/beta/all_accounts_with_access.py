from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AllAccountsWithAccess(BaseModel):
	odata_type: Literal["#microsoft.graph.allAccountsWithAccess"] = Field(alias="@odata.type", default="#microsoft.graph.allAccountsWithAccess")


