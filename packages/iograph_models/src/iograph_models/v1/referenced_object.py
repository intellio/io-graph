from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReferencedObject(BaseModel):
	referencedObjectName: Optional[str] = Field(alias="referencedObjectName", default=None,)
	referencedProperty: Optional[str] = Field(alias="referencedProperty", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


