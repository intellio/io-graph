from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ReferenceCreate(BaseModel):
	odata_id: Optional[str] = Field(alias="@odata.id",default=None,)


