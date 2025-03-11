from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityFilePlanCitation(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	citationJurisdiction: Optional[str] = Field(alias="citationJurisdiction",default=None,)
	citationUrl: Optional[str] = Field(alias="citationUrl",default=None,)


