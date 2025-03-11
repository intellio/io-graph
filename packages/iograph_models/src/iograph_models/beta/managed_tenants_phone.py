from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsPhone(BaseModel):
	phoneNumber: Optional[str] = Field(alias="phoneNumber",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


