from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewReviewerScope(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	query: Optional[str] = Field(alias="query",default=None,)
	queryRoot: Optional[str] = Field(alias="queryRoot",default=None,)
	queryType: Optional[str] = Field(alias="queryType",default=None,)


