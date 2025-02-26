from __future__ import annotations
from pydantic import BaseModel, Field


class Security_apply_tagsPostRequest(BaseModel):
	tagsToAdd: list[SecurityEdiscoveryReviewTag] = Field(alias="tagsToAdd",)
	tagsToRemove: list[SecurityEdiscoveryReviewTag] = Field(alias="tagsToRemove",)

from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag
from .security_ediscovery_review_tag import SecurityEdiscoveryReviewTag

