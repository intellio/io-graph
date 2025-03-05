from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignedLicense(BaseModel):
	disabledPlans: Optional[list[UUID]] = Field(alias="disabledPlans",default=None,)
	skuId: Optional[UUID] = Field(alias="skuId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


