from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RubricQualitySelectedColumnModel(BaseModel):
	columnId: Optional[str] = Field(alias="columnId",default=None,)
	qualityId: Optional[str] = Field(alias="qualityId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


