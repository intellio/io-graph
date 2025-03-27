from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Ediscovery_add_to_review_setPostRequest(BaseModel):
	sourceCollection: Optional[EdiscoverySourceCollection] = Field(alias="sourceCollection", default=None,)
	additionalDataOptions: Optional[EdiscoveryAdditionalDataOptions | str] = Field(alias="additionalDataOptions", default=None,)

from .ediscovery_source_collection import EdiscoverySourceCollection
from .ediscovery_additional_data_options import EdiscoveryAdditionalDataOptions

