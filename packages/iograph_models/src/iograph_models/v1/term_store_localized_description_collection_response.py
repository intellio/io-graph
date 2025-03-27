from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TermStoreLocalizedDescriptionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[TermStoreLocalizedDescription]] = Field(alias="value", default=None,)

from .term_store_localized_description import TermStoreLocalizedDescription

