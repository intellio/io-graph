from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EdgeSearchEngineCustom(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	edgeSearchEngineOpenSearchXmlUrl: Optional[str] = Field(alias="edgeSearchEngineOpenSearchXmlUrl",default=None,)


