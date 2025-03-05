from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrincipalResourceMembershipsScope(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	principalScopes: SerializeAsAny[Optional[list[AccessReviewScope]]] = Field(default=None,alias="principalScopes",)
	resourceScopes: SerializeAsAny[Optional[list[AccessReviewScope]]] = Field(default=None,alias="resourceScopes",)

from .access_review_scope import AccessReviewScope
from .access_review_scope import AccessReviewScope

