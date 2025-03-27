from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class TransformationAttribute(BaseModel):
	attribute: Optional[Union[SourcedAttribute, ValueBasedAttribute]] = Field(alias="attribute", default=None,discriminator="odata_type", )
	treatAsMultiValue: Optional[bool] = Field(alias="treatAsMultiValue", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .sourced_attribute import SourcedAttribute
from .value_based_attribute import ValueBasedAttribute

