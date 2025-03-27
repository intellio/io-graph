from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyPresentationValueCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[GroupPolicyPresentationValueBoolean, GroupPolicyPresentationValueDecimal, GroupPolicyPresentationValueList, GroupPolicyPresentationValueLongDecimal, GroupPolicyPresentationValueMultiText, GroupPolicyPresentationValueText],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .group_policy_presentation_value_boolean import GroupPolicyPresentationValueBoolean
from .group_policy_presentation_value_decimal import GroupPolicyPresentationValueDecimal
from .group_policy_presentation_value_list import GroupPolicyPresentationValueList
from .group_policy_presentation_value_long_decimal import GroupPolicyPresentationValueLongDecimal
from .group_policy_presentation_value_multi_text import GroupPolicyPresentationValueMultiText
from .group_policy_presentation_value_text import GroupPolicyPresentationValueText

