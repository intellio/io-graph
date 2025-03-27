from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InstantiatePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	serviceManagementReference: Optional[str] = Field(alias="serviceManagementReference", default=None,)


