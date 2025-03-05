from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceAction(BaseModel):
	allowedResourceActions: Optional[list[str]] = Field(alias="allowedResourceActions",default=None,)
	notAllowedResourceActions: Optional[list[str]] = Field(alias="notAllowedResourceActions",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


