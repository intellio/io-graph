from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class JobResponseBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[JobResponseBase]]] = Field(alias="value",default=None,)

from .job_response_base import JobResponseBase

