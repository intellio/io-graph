from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_assignment_filters_status_detailsPostRequest(BaseModel):
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	payloadId: Optional[str] = Field(alias="payloadId", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	assignmentFilterIds: Optional[list[str]] = Field(alias="assignmentFilterIds", default=None,)
	top: Optional[int] = Field(alias="top", default=None,)
	skip: Optional[int] = Field(alias="skip", default=None,)

