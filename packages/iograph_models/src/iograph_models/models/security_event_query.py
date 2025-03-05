from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEventQuery(BaseModel):
	query: Optional[str] = Field(alias="query",default=None,)
	queryType: Optional[SecurityQueryType | str] = Field(alias="queryType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_query_type import SecurityQueryType

