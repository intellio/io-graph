from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationError(BaseModel):
	code: Optional[str] = Field(default=None,alias="code",)
	message: Optional[str] = Field(default=None,alias="message",)
	tenantActionable: Optional[bool] = Field(default=None,alias="tenantActionable",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


