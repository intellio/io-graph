from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExactMatchDataStore(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.exactMatchDataStore"] = Field(alias="@odata.type", default="#microsoft.graph.exactMatchDataStore")
	columns: Optional[list[ExactDataMatchStoreColumn]] = Field(alias="columns", default=None,)
	dataLastUpdatedDateTime: Optional[datetime] = Field(alias="dataLastUpdatedDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	sessions: Optional[list[ExactMatchSession]] = Field(alias="sessions", default=None,)

from .exact_data_match_store_column import ExactDataMatchStoreColumn
from .exact_match_session import ExactMatchSession
