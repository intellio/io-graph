from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PrincipalResourceMembershipsScope(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	principalScopes: list[AccessReviewScope] = Field(alias="principalScopes",)
	resourceScopes: list[AccessReviewScope] = Field(alias="resourceScopes",)

from .access_review_scope import AccessReviewScope
from .access_review_scope import AccessReviewScope

