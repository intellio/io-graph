from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class My_requestsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[PrivilegedApproval]] = Field(alias="value", default=None,)

from .privileged_approval import PrivilegedApproval

