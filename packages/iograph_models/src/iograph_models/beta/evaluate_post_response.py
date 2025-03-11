from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EvaluatePostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ConditionalAccessWhatIfPolicy]] = Field(alias="value",default=None,)

from .conditional_access_what_if_policy import ConditionalAccessWhatIfPolicy

