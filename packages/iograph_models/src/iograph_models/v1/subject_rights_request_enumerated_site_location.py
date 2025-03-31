from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SubjectRightsRequestEnumeratedSiteLocation(BaseModel):
	odata_type: Literal["#microsoft.graph.subjectRightsRequestEnumeratedSiteLocation"] = Field(alias="@odata.type", default="#microsoft.graph.subjectRightsRequestEnumeratedSiteLocation")
	urls: Optional[list[str]] = Field(alias="urls", default=None,)

