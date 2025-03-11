from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Import_resource_actionsPostRequest(BaseModel):
	format: Optional[str] = Field(alias="format",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	overwriteResourceNamespace: Optional[bool] = Field(alias="overwriteResourceNamespace",default=None,)


