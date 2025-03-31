from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Clean_windows_devicePostRequest(BaseModel):
	keepUserData: Optional[bool] = Field(alias="keepUserData", default=None,)

