from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EnablePostRequest(BaseModel):
	appOwnerTenantId: Optional[str] = Field(default=None,alias="appOwnerTenantId",)


