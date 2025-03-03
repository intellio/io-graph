from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthorizationInfo(BaseModel):
	certificateUserIds: Optional[list[str]] = Field(default=None,alias="certificateUserIds",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


