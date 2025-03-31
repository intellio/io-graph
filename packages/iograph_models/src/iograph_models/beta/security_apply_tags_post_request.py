from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_apply_tagsPostRequest(BaseModel):
	tagsToAdd: Optional[list[SecurityEdiscoveryReviewTag]] = Field(alias="tagsToAdd", default=None,)
	tagsToRemove: Optional[list[SecurityEdiscoveryReviewTag]] = Field(alias="tagsToRemove", default=None,)

from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag
