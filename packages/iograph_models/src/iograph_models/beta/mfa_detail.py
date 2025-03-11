from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MfaDetail(BaseModel):
	authDetail: Optional[str] = Field(alias="authDetail",default=None,)
	authMethod: Optional[str] = Field(alias="authMethod",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


