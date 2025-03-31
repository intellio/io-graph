from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessReviewNotificationRecipientQueryScope(BaseModel):
	odata_type: Literal["#microsoft.graph.accessReviewNotificationRecipientQueryScope"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewNotificationRecipientQueryScope")
	query: Optional[str] = Field(alias="query", default=None,)
	queryRoot: Optional[str] = Field(alias="queryRoot", default=None,)
	queryType: Optional[str] = Field(alias="queryType", default=None,)

