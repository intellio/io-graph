from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class InstantiatePostRequest(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	serviceManagementReference: Optional[str] = Field(default=None,alias="serviceManagementReference",)


