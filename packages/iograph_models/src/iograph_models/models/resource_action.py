from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceAction(BaseModel):
	allowedResourceActions: Optional[list[str]] = Field(default=None,alias="allowedResourceActions",)
	notAllowedResourceActions: Optional[list[str]] = Field(default=None,alias="notAllowedResourceActions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


