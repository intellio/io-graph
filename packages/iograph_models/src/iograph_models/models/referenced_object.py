from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReferencedObject(BaseModel):
	referencedObjectName: Optional[str] = Field(default=None,alias="referencedObjectName",)
	referencedProperty: Optional[str] = Field(default=None,alias="referencedProperty",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


