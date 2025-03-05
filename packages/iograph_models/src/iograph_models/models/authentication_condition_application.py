from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationConditionApplication(BaseModel):
	appId: Optional[str] = Field(default=None,alias="appId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


