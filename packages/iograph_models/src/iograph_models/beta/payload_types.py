from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PayloadTypes(BaseModel):
	rawContent: Optional[str] = Field(alias="rawContent",default=None,)
	visualContent: Optional[VisualProperties] = Field(alias="visualContent",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .visual_properties import VisualProperties

