from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SubjectRightsRequestAllSiteLocation(BaseModel):
	odata_type: Literal["#microsoft.graph.subjectRightsRequestAllSiteLocation"] = Field(alias="@odata.type", default="#microsoft.graph.subjectRightsRequestAllSiteLocation")

