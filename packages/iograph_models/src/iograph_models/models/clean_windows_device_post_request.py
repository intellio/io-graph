from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Clean_windows_devicePostRequest(BaseModel):
	keepUserData: Optional[bool] = Field(default=None,alias="keepUserData",)


