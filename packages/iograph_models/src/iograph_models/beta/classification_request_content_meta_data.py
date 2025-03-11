from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClassificationRequestContentMetaData(BaseModel):
	sourceId: Optional[str] = Field(alias="sourceId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


