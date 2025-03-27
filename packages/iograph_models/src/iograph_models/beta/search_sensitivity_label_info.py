from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SearchSensitivityLabelInfo(BaseModel):
	color: Optional[str] = Field(alias="color", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	priority: Optional[int] = Field(alias="priority", default=None,)
	sensitivityLabelId: Optional[str] = Field(alias="sensitivityLabelId", default=None,)
	tooltip: Optional[str] = Field(alias="tooltip", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


