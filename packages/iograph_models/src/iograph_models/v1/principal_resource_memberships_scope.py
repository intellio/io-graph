from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class PrincipalResourceMembershipsScope(BaseModel):
	odata_type: Literal["#microsoft.graph.principalResourceMembershipsScope"] = Field(alias="@odata.type", default="#microsoft.graph.principalResourceMembershipsScope")
	principalScopes: Optional[list[Annotated[Union[AccessReviewInactiveUsersQueryScope, PrincipalResourceMembershipsScope],Field(discriminator="odata_type")]]] = Field(alias="principalScopes", default=None,)
	resourceScopes: Optional[list[Annotated[Union[AccessReviewInactiveUsersQueryScope, PrincipalResourceMembershipsScope],Field(discriminator="odata_type")]]] = Field(alias="resourceScopes", default=None,)

from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
