from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesDirectorySynchronizationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OnPremisesDirectorySynchronization] = Field(alias="value",)

from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization

