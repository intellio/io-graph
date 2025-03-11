from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrincipalResourceMembershipsScope(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	principalScopes: SerializeAsAny[Optional[list[AccessReviewScope]]] = Field(alias="principalScopes",default=None,)
	resourceScopes: SerializeAsAny[Optional[list[AccessReviewScope]]] = Field(alias="resourceScopes",default=None,)

from .access_review_scope import AccessReviewScope
from .access_review_scope import AccessReviewScope

