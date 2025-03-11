from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsEmail(BaseModel):
	emailAddress: Optional[str] = Field(alias="emailAddress",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


