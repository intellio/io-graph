from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SubjectRightsRequestAllMailboxLocation(BaseModel):
	odata_type: Literal["#microsoft.graph.subjectRightsRequestAllMailboxLocation"] = Field(alias="@odata.type", default="#microsoft.graph.subjectRightsRequestAllMailboxLocation")

