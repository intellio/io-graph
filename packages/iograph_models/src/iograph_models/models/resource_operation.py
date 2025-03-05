from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResourceOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	actionName: Optional[str] = Field(default=None,alias="actionName",)
	description: Optional[str] = Field(default=None,alias="description",)
	resourceName: Optional[str] = Field(default=None,alias="resourceName",)


