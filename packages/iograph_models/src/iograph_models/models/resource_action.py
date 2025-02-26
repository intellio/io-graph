from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ResourceAction(BaseModel):
	allowedResourceActions: list[Optional[str]] = Field(alias="allowedResourceActions",)
	notAllowedResourceActions: list[Optional[str]] = Field(alias="notAllowedResourceActions",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


