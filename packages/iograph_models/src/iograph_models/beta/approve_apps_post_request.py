from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Approve_appsPostRequest(BaseModel):
	packageIds: Optional[list[str]] = Field(alias="packageIds", default=None,)
	approveAllPermissions: Optional[bool] = Field(alias="approveAllPermissions", default=None,)

