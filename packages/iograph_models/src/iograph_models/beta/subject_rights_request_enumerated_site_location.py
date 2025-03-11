from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SubjectRightsRequestEnumeratedSiteLocation(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	urls: Optional[list[str]] = Field(alias="urls",default=None,)


