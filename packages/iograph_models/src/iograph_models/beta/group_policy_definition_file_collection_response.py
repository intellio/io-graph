from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyDefinitionFileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[GroupPolicyUploadedDefinitionFile],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .group_policy_uploaded_definition_file import GroupPolicyUploadedDefinitionFile

