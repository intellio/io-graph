from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Security_add_to_review_setPostRequest(BaseModel):
	search: Optional[SecurityEdiscoverySearch] = Field(default=None,alias="search",)
	additionalDataOptions: Optional[SecurityAdditionalDataOptions] = Field(default=None,alias="additionalDataOptions",)

from .security_ediscovery_search import SecurityEdiscoverySearch
from .security_additional_data_options import SecurityAdditionalDataOptions

