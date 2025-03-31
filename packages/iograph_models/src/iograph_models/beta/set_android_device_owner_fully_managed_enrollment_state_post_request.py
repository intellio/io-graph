from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Set_android_device_owner_fully_managed_enrollment_statePostRequest(BaseModel):
	enabled: Optional[bool] = Field(alias="enabled", default=None,)

