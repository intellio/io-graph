from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessAssociatedBranch(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	branchId: Optional[str] = Field(alias="branchId",default=None,)


