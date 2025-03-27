from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInactiveUsersQueryScope(BaseModel):
	odata_type: Literal["#microsoft.graph.accessReviewInactiveUsersQueryScope"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewInactiveUsersQueryScope")
	query: Optional[str] = Field(alias="query", default=None,)
	queryRoot: Optional[str] = Field(alias="queryRoot", default=None,)
	queryType: Optional[str] = Field(alias="queryType", default=None,)
	inactiveDuration: Optional[str] = Field(alias="inactiveDuration", default=None,)


