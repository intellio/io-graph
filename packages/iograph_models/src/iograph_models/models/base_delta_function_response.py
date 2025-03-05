from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BaseDeltaFunctionResponse(BaseModel):
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	odata_deltaLink: Optional[str] = Field(alias="@odata.deltaLink",default=None,)


