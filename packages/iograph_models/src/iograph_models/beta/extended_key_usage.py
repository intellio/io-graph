from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExtendedKeyUsage(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	objectIdentifier: Optional[str] = Field(alias="objectIdentifier",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


