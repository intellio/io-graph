from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class CustomClaimTransformationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[ContainsTransformation, EndsWithTransformation, ExtractAlphaTransformation, ExtractMailPrefixTransformation, ExtractNumberTransformation, ExtractTransformation, IfEmptyTransformation, IfNotEmptyTransformation, JoinTransformation, RegexReplaceTransformation, StartsWithTransformation, SubstringTransformation, ToLowercaseTransformation, ToUppercaseTransformation, TrimTransformation]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .contains_transformation import ContainsTransformation
from .ends_with_transformation import EndsWithTransformation
from .extract_alpha_transformation import ExtractAlphaTransformation
from .extract_mail_prefix_transformation import ExtractMailPrefixTransformation
from .extract_number_transformation import ExtractNumberTransformation
from .extract_transformation import ExtractTransformation
from .if_empty_transformation import IfEmptyTransformation
from .if_not_empty_transformation import IfNotEmptyTransformation
from .join_transformation import JoinTransformation
from .regex_replace_transformation import RegexReplaceTransformation
from .starts_with_transformation import StartsWithTransformation
from .substring_transformation import SubstringTransformation
from .to_lowercase_transformation import ToLowercaseTransformation
from .to_uppercase_transformation import ToUppercaseTransformation
from .trim_transformation import TrimTransformation

