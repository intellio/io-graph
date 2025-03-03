from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Security_apply_tagsPostRequest(BaseModel):
	tagsToAdd: Optional[list[SecurityEdiscoveryReviewTag]] = Field(default=None,alias="tagsToAdd",)
	tagsToRemove: Optional[list[SecurityEdiscoveryReviewTag]] = Field(default=None,alias="tagsToRemove",)

from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag
from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag

