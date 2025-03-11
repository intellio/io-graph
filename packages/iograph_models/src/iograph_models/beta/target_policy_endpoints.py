from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TargetPolicyEndpoints(BaseModel):
	platformTypes: Optional[list[str]] = Field(alias="platformTypes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


