from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentFilterState(BaseModel):
	enabled: Optional[bool] = Field(alias="enabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


