from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignedLicense(BaseModel):
	disabledPlans: Optional[list[UUID]] = Field(default=None,alias="disabledPlans",)
	skuId: Optional[UUID] = Field(default=None,alias="skuId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


