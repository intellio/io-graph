from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Parse_expressionPostRequest(BaseModel):
	expression: Optional[str] = Field(alias="expression", default=None,)
	testInputObject: Optional[ExpressionInputObject] = Field(alias="testInputObject", default=None,)
	targetAttributeDefinition: Optional[AttributeDefinition] = Field(alias="targetAttributeDefinition", default=None,)

from .expression_input_object import ExpressionInputObject
from .attribute_definition import AttributeDefinition

