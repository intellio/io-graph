from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OpenShiftChangeRequestCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OpenShiftChangeRequest] = Field(alias="value",)

from .open_shift_change_request import OpenShiftChangeRequest

