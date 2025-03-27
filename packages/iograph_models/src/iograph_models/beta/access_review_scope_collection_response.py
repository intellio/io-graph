from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewScopeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AccessReviewQueryScope, AccessReviewInactiveUsersQueryScope, AccessReviewReviewerScope, PrincipalResourceMembershipsScope],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .access_review_query_scope import AccessReviewQueryScope
from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
from .access_review_reviewer_scope import AccessReviewReviewerScope
from .principal_resource_memberships_scope import PrincipalResourceMembershipsScope

