from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddIn(BaseModel):
	id: Optional[UUID] = Field(default=None,alias="id",)
	properties: Optional[list[KeyValue]] = Field(default=None,alias="properties",)
	type: Optional[str] = Field(default=None,alias="type",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .key_value import KeyValue

