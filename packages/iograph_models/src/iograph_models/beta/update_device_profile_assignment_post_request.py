from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Update_device_profile_assignmentPostRequest(BaseModel):
	deviceIds: Optional[list[str]] = Field(alias="deviceIds", default=None,)

