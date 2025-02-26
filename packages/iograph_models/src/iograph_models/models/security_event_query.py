from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEventQuery(BaseModel):
	query: Optional[str] = Field(default=None,alias="query",)
	queryType: Optional[SecurityQueryType] = Field(default=None,alias="queryType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_query_type import SecurityQueryType

