from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExactMatchLookupJob(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.exactMatchLookupJob"] = Field(alias="@odata.type", default="#microsoft.graph.exactMatchLookupJob")
	completionDateTime: Optional[datetime] = Field(alias="completionDateTime", default=None,)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	error: Optional[ClassificationError] = Field(alias="error", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	matchingRows: Optional[list[LookupResultRow]] = Field(alias="matchingRows", default=None,)

from .classification_error import ClassificationError
from .lookup_result_row import LookupResultRow
